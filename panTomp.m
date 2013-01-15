% pantompkins with heart beat detection
% Orginally from:
% http://www.mathworks.com/matlabcentral/fileexchange/31307-pan-thompkins-algoritim-implementation/content/pantompkins.m
% abhijit_bailur@yahoo.co.in 
clc;
clear all
close all
load('806m.mat');
x1=val(1,1:800);
y=length(x1);
fs = 128;              
N = length (x1);       
t = [0:N-1]/fs;        
figure(1)
subplot(2,1,1)
plot(t,x1)
subplot(2,1,2)
plot(t(200:600),x1(200:600))
xlim([1 3])

x1 = x1 - mean (x1 );    
x1 = x1/ max( abs(x1 )) ;
figure(2)
subplot(2,1,1)
plot(t,x1)
subplot(2,1,2)
plot(t(200:600),x1(200:600))
xlim([1 3])

b=[1 0 0 0 0 0 -2 0 0 0 0 0 1];
a=[1 -2 1];
h=filter(b,a,[1 zeros(1,12)]); 
x2 = conv (x1 ,h);
x2 = x2/ max( abs(x2 )); 
figure(3)
subplot(2,1,1)
plot([0:length(x2)-1]/fs,x2)
xlim([0 max(t)])
subplot(2,1,2)
plot(t(200:600),x2(200:600))
xlim([1 3])

b = [-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 32 -32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1];
a = [1 -1];
h1=filter(b,a,[1 zeros(1,32)]); 
x3 = conv (x2 ,h1);
x3 = x3/ max( abs(x3 ));
figure(4)
subplot(2,1,1)
plot([0:length(x3)-1]/fs,x3)
xlim([0 max(t)])
subplot(2,1,2)
plot(t(200:600),x3(200:600))
xlim([1 3])

h = [-1 -2 0 2 1]/8;
x4 = conv (x3 ,h);
x4 = x4 (2+[1: N]);
x4 = x4/ max( abs(x4 ));
figure(5)
subplot(2,1,1)
plot([0:length(x4)-1]/fs,x4)
subplot(2,1,2)
plot(t(200:600),x4(200:600))
xlim([1 3])

x5 = x4 .^2;
x5 = x5/ max( abs(x5 ));
figure(6)
subplot(2,1,1)
plot([0:length(x5)-1]/fs,x5)
subplot(2,1,2)
plot(t(200:600),x5(200:600))
xlim([1 3])

h = ones (1 ,31)/31;
Delay = 15; 
x6 = conv (x5 ,h);
x6 = x6 (15+[1: N]);
x6 = x6/ max( abs(x6 ));
figure(7)
subplot(2,1,1)
plot([0:length(x6)-1]/fs,x6)
subplot(2,1,2)
plot(t(200:600),x6(200:600))
xlim([1 3])
figure(7)
subplot(2,1,1)

max1 = max(x6);
thresh = mean (x6 );
k=thresh*max1;
y =(x6>k)';
figure,plot(y,t)
figure (8)
subplot(2,1,1)
plot (t(200:600),x1(200:600)/max(x1))
box on
xlim([1 3])
subplot(2,1,2)
plot (t(200:600),x6(200:600)/max(x6))
xlim([1 3])

left = find(diff([0 y'])==1);
right = find(diff([y' 0])==-1);
left=left-20;
for i=1:length(left)
   [Rv(i) Rl(i)] = max( x1(left(i):right(i)) );
   Rl(i) = Rl(i)+left(i) ;
   for j=1:20
   x(j)=left(j);
  for l=1:20;
  k(l)=left(j)-left(j+1);
  y=-1*mean2(k(l));
  end
 end
   end
figure
plot (t,x1/max(x1) , t(Rl) ,Rv , 'r*');
xlim([1 3])
heartrate=(fs*60)/y;
tx=0:N-1/fs;
figure,plot(tx(200:600),x1(200:600))
disp('HEART RATE IS:::')
fprintf('%d\n', round(heartrate));
if (heartrate==72)
disp('HEART RATE OF THE SUBJECT IS NORMAL');
end
if(heartrate<72)
disp('HEART RATE OF THE SUBJECT IS BELOW NORMAL ,THE SUBJECT IS SUFFERING FROM BRADYCARDIA');
else
disp('HEART RATE OF THE SUBJECT IS ABOVE NORMAL ,THE SUBJECT IS SUFFERING FROM TRACHYCARDIA');
end
