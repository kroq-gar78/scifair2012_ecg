 % Load original 1D signal.
%clc;
%clear all;
close all;
ELEVATED=[];
%[fname path]=uigetfile('*.mat');
%fname=strcat(path,fname);
rnum = '100';
        load(strcat(rnum,'m.mat'));
       %val=val(1:15000);
       z=zeros(100,1);
       samplingrate=360;
       A=val(1,:);
       %v1=val(1,:)-val(1,1);
       v1=val(1,:);
       A=v1;
       A=A';
       zc=A(1);
       %A=[z;A;z];
       
       
      %  s = A(1:1:400);
        s = A;
        
        ls = length(s);
        %{
figure(1)
        plot(s);
        title('Actual Signal'),grid on
        %}

  %[c,l]=wavedec(s,4,'db4');
  %ca1=appcoef(c,l,'db4',1);
  %ca2=appcoef(c,l,'db4',2);
  %ca3=appcoef(c,l,'db4',3);
  %ca4=appcoef(c,l,'db4',4);
  
  %{
figure(2)
  plot(c),title('decomposed signal'),grid on
  figure(3)
  subplot(2,2,1)
  plot(ca1),title('1st level reconstructed'),grid on
    subplot(2,2,2)
  plot(ca2),title('2nd level reconstructed'),grid on
    subplot(2,2,3)
  plot(ca3),title('3rd level reconstructed'),grid on
    subplot(2,2,4)
  plot(ca4),title('4th level reconstructed'),grid on
 %} 
  

  

  
  %{
figure(4)
  plot(y),grid on
  title('base line corrected and smoothed signal')
  %}
  
  %% DETECT R PEAK
%% Calculate R in the actual Signal
ecg=A;

% no filter
A=A-1024;
corrected=A;

%{
% FFTW filter
fresult=fft(A);
fresult(1 : round(length(fresult)*5/samplingrate))=0;
fresult(end - round(length(fresult)*5/samplingrate) : end)=0;
corrected=real(ifft(fresult));
%}
%{
% moving average filter
window = 15;
h = ones(window,1)/window;
corrected = filter(h, 1, A);
%}

% lowpass Butterworth filter
fNorm = 25 / (samplingrate/2);               %# normalized cutoff frequency
[b,a] = butter(10, fNorm, 'low');  %# 10th order filter
corrected = filtfilt(b, a, A);

%   Filter - first pass
WinSize = floor(samplingrate * 571 / 1000);
if rem(WinSize,2)==0
    WinSize = WinSize+1;
end
filtered1=librow_winmax(corrected, WinSize);
%   Scale ecg
peaks1=filtered1/(max(filtered1)/7);
%peaks1=filtered1;
%   Filter by threshold filter
for data = 1:1:length(peaks1)
    if peaks1(data) < 4
        peaks1(data) = 0;
    else
        peaks1(data)=1;
    end
end
positions=find(peaks1);
distance=positions(2)-positions(1);
for data=1:1:length(positions)-1
    if positions(data+1)-positions(data)<distance
        distance=positions(data+1)-positions(data);
    end
end
% Optimize filter window size
QRdistance=floor(0.04*samplingrate);
if rem(QRdistance,2)==0
    QRdistance=QRdistance+1;
end
WinSize=2*distance-QRdistance;
% Filter - second pass
filtered2=librow_winmax(corrected, WinSize);
peaks2=filtered2;
for data=1:1:length(peaks2)
    if peaks2(data)<4
        peaks2(data)=0;
    else
        peaks2(data)=1;
    end
end
Rloc=find(peaks2);
Ramp=A(Rloc);
%% After R Peak Tracking detect others
% Work from closest to R peak to farthest from R peak
y1=A;

% matrices to mark indeces for removal due to them being too close to the start/end
rvalsToKill = [];
qvalsToKill = [];
pvalsToKill = [];
svalsToKill = [];
for(j=1:1:length(Rloc))
    %% Q  Detection
    startpt=Rloc(j)-100;
    if startpt<1
        startpt=1;
    end
    endpt=Rloc(j)-10;
    if endpt>length(A)
        endpt=length(A);
    end
    if startpt>=endpt
        % mark indeces to kill because the feature's range is bad
        rvalsToKill = [rvalsToKill;j]
        continue
    end
    a=startpt:endpt;
    m=min(y1(a));
    b=find(y1(a)==m);
    b=b(1);
    b=a(b);
    Qloc(j)=b;
    Qamp(j)=m;
%% P Peak
    try
    
    startpt=Qloc(j)-100;
    if startpt<1
        startpt=1;
    end
    endpt=Qloc(j)-10;
    if endpt>length(A)
        endpt=length(A);
    end
    if startpt>=endpt
        % mark indeces to kill because the feature's range is bad
        rvalsToKill = [rvalsToKill;j]
        qvalsToKill = [qvalsToKill;j];
        continue
    end
    a=startpt:endpt;
    m=max(y1(a));
    b=find(y1(a)==m);
    b=b(1);
    b=a(b);
    Ploc(j)=b;
    Pamp(j)=m;
        
    end

    %% S  Detection
    
    startpt=Rloc(j)+5;
    if startpt<1
        startpt=1;
    end
    endpt=Rloc(j)+50;
    if endpt>length(A)
        endpt=length(A);
    end
    if startpt>=endpt
        % mark indeces to kill because the feature's range is bad
        rvalsToKill = [rvalsToKill;j]
        qvalsToKill = [qvalsToKill;j];
        pvalsToKill = [pvalsToKill;j];
        continue
    end
    a=startpt:endpt;
    m=min(y1(a));
    b=find(y1(a)==m);
    b=b(1);
    b=a(b);
    Sloc(j)=b;
    Samp(j)=m;
    
    %% T Peak
    startpt=Sloc(j)+10;
    if startpt<1
        startpt=1;
    end
    endpt=Sloc(j)+70;
    if endpt>length(A)
        endpt=length(A);
    end
    if startpt>=endpt
        % mark indeces to kill because the feature's range is bad
        rvalsToKill = [rvalsToKill;j]
        qvalsToKill = [qvalsToKill;j];
        pvalsToKill = [pvalsToKill;j];
        svalsToKill = [svalsToKill;j];
        continue
    end
    a=startpt:endpt;
    m=max(y1(a));
    b=find(y1(a)==m);
    b=b(1);
    b=a(b);
    Tloc(j)=b;
    Tamp(j)=m;
end

% delete all values marked for deletion
for(j=rvalsToKill)
    Rloc(j) = [];
    Ramp(j) = [];
end
for(j=qvalsToKill)
    Qloc(j) = [];
    Qamp(j) = [];
end
for(j=pvalsToKill)
    Ploc(j) = [];
    Pamp(j) = [];
end
for(j=svalsToKill)
    Sloc(j) = [];
    Samp(j) = [];
end

%figure;
%subplot(6,1,k);
    
%{
plot(y1), hold on;
plot(Rloc,Ramp,'*'),hold on;
plot(Qloc,Qamp,'+'),hold on;
plot(Sloc,Samp,'+'),hold on;
plot(Ploc,Pamp,'^'), hold on
plot(Tloc,Tamp,'^')
grid on;
%}

% Write points to files
%{
for i=1:1:length(Rloc)
    fprintf(fopen(strcat(rnum,'_r.txt'),'w'),'%d,%d\n',[Rloc(i);Ramp(i)]);
end
%}

% manipulate variables such that matlab doesn't mess them up
% while writing to CSV files (loss of precision after ~100,000)


%fprintf(fopen(strcat(rnum,'_r.txt'),'w'),'%d,%d\n',[Rloc';Ramp]);
%csvwrite(strcat(rnum,'_r.csv'),[Rloc',Ramp]);
%csvwrite(strcat(rnum,'_p.csv'),[Ploc',Pamp']);
%csvwrite(strcat(rnum,'_q.csv'),[Qloc',Qamp']);
%csvwrite(strcat(rnum,'_s.csv'),[Sloc',Samp']);
%csvwrite(strcat(rnum,'_t.csv'),[Tloc',Tamp']);
Rloc=Rloc';
Ploc=Ploc';
Pamp=Pamp';
Qloc=Qloc';
Qamp=Qamp';
Sloc=Sloc';
Samp=Samp';
Tloc=Tloc';
Tamp=Tamp';
save(strcat(rnum,'_r.mat'),'Rloc','Ramp');
save(strcat(rnum,'_p.mat'),'Ploc','Pamp');
save(strcat(rnum,'_q.mat'),'Qloc','Qamp');
save(strcat(rnum,'_s.mat'),'Sloc','Samp');
save(strcat(rnum,'_t.mat'),'Tloc','Tamp');
