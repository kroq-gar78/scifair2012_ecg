tar cjf ./old.tar.bz2 `find . -type d -not -path './.git*' -not -path './ECG_FEATURE_WAVELET_ST*' -not -name 'timestr' -not -name '.'|xargs`
