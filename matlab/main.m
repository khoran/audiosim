% Clean-up MATLAB's environment
clear all; close all; clc;  

% Define variables
Tw = 50;                % analysis frame duration (ms)
Ts = 20;                % analysis frame shift (ms)
alpha = 0.97;           % preemphasis coefficient
M = 20;                 % number of filterbank channels 
C = 12;                 % number of cepstral coefficients
L = 22;                 % cepstral sine lifter parameter
LF = 300;               % lower frequency limit (Hz)
HF = 3700;              % upper frequency limit (Hz)
EThres = 0.7;           % threshold for short-time energy in each frame
W = 100;                % window parameter for DTW if s(i) is matched with 
                        % t(j) then |i-j|<=w
wav_file{1}= 'A01420-01_10secA.wav';  % input audio filename
wav_file{2} = 'A01420-01_10secB.wav';  % input audio filename
wav_file{3} = 'A01420-01_10secC.wav';  % input audio filename
wav_file{4} = 'A01420-02_10secA.wav';  % input audio filename
wav_file{5} = 'A01420-02_10secB.wav';  % input audio filename
wav_file{6} = 'A01420-02_10secC.wav';  % input audio filename
wav_file{7} = 'A01420-03_10secA.wav';  % input audio filename
wav_file{8} = 'A01420-03_10secB.wav';  % input audio filename
wav_file{9} = 'A01420-03_10secC.wav';  % input audio filename
wav_file{10} = 'A01420-04_10secA.wav';  % input audio filename
wav_file{11} = 'A01420-04_10secB.wav';  % input audio filename
wav_file{12} = 'A01420-04_10secC.wav';  % input audio filename
wav_file{13} = 'A09550-01_10secA.wav';  % input audio filename
wav_file{14} = 'A09550-01_10secB.wav';  % input audio filename
wav_file{15} = 'A09550-01_10secC.wav';  % input audio filename
wav_file{16} = 'A20760-01_10secA.wav';  % input audio filename
wav_file{17} = 'A20760-01_10secB.wav';  % input audio filename
wav_file{18} = 'A20760-01_10secC.wav';  % input audio filename
wav_file{19} = 'A20760-02_10secA.wav';  % input audio filename
wav_file{20} = 'A20760-02_10secB.wav';  % input audio filename
wav_file{21} = 'A20760-02_10secC.wav';  % input audio filename
wav_file{22} = 'A20760-03_10secA.wav';  % input audio filename
wav_file{23} = 'A20760-03_10secB.wav';  % input audio filename
wav_file{24} = 'A20760-03_10secC.wav';  % input audio filename
wav_file{25} = 'A20760-04_10secA.wav';  % input audio filename
wav_file{26} = 'A20760-04_10secB.wav';  % input audio filename
wav_file{27} = 'A20760-04_10secC.wav';  % input audio filename
wav_file{28} = 'A71790-02_10secA.wav';  % input audio filename
wav_file{29} = 'A71790-02_10secB.wav';  % input audio filename
wav_file{30} = 'A71790-02_10secC.wav';  % input audio filename
wav_file{31} = 'A76900-02_10secA.wav';  % input audio filename
wav_file{32} = 'A76900-02_10secB.wav';  % input audio filename
wav_file{33} = 'A76900-02_10secC.wav';  % input audio filename
wav_file{34} = 'A76900-03_10secA.wav';  % input audio filename
wav_file{35} = 'A76900-03_10secB.wav';  % input audio filename
wav_file{36} = 'A76900-03_10secC.wav';  % input audio filename
wav_file{37} = 'A76900-04_10secA.wav';  % input audio filename
wav_file{38} = 'A76900-04_10secB.wav';  % input audio filename
wav_file{39} = 'A76900-04_10secC.wav';  % input audio filename

comparison_matrix = zeros(13,13);

for i = 1:3:37
for j = 1:3:37

% Read speech samples, sampling raecision from file
[ speech1, fs1 ] = audioread( wav_file{i} );
%speech1 = (speech1(:,1)+speech1(:,2))/2;
[ speech2, fs2 ] = audioread( wav_file{j} );
%speech2 = (speech2(:,1)+speech2(:,2))/2;

% Feature extraction (feature vectors as columns)
[ MFCCs1, FBEs1, frames1 ] = ...
	mfcc( speech1, fs1, Tw, Ts, alpha, @hamming, [LF HF], M, C+1, L );
[ MFCCs2, FBEs2, frames2 ] = ...
	mfcc( speech2, fs2, Tw, Ts, alpha, @hamming, [LF HF], M, C+1, L );

% Eliminate unvoiced frames using short-time energy
frame_num1 = size(FBEs1,2);
frame_energy1 = zeros(1,frame_num1);
for frame_index=1:frame_num1
    frame_energy1(1,frame_index) = sum(FBEs1(:,frame_index));
end
ave_energy1 = mean(frame_energy1);
counter1 = 0;
for frame_index=1:frame_num1
    if (frame_energy1(1,frame_index) < (EThres*ave_energy1))
        MFCCs1(:,frame_index-counter1) = [];
    end
    counter1 = counter1 + 1;
end

frame_num2 = size(FBEs2,2);
frame_energy2 = zeros(1,frame_num2);
for frame_index=1:frame_num2
    frame_energy2(1,frame_index) = sum(FBEs2(:,frame_index));
end
ave_energy2 = mean(frame_energy2);
counter2 = 0;
for frame_index=1:frame_num2
    if (frame_energy2(1,frame_index) < (EThres*ave_energy2))
        MFCCs2(:,frame_index-counter2) = [];
    end
    counter2 = counter2 + 1;
end

% Dynamic time warping of two signals
d = dtw_c(MFCCs1',MFCCs2',W);
fprintf('resulting distance(%d,%d)=%f\n',(i+2)/3,(j+2)/3,d);
if (d < 1)
    comparison_matrix((i+2)/3,(j+2)/3) = 1e+10;
else
    comparison_matrix((i+2)/3,(j+2)/3) = d;
end

end
end