% this script is to simulate the reconstruction principle of PALM
% Author: RiwangChen <chenriwang@pku.edu.cn> 2021-11-1
close all;
clear;

imStack = ReadTif('TestPALM.tif'); % load images 
framNum = size(imStack,3);% the number of the input images

% d = 80; % resolution
% L = 4; % range
% X = 7.5; % X-center
% Y = 8.5; % Y-center

% idx = X-L/2:L/d:X+L/2;
% idy = Y-L/2:L/d:Y+L/2;
idx = 5.5:0.05:9.5; 
idy = 6.5:0.05:10.5; 

g = 1; % the overall gain of the imaging system
b = 5/g; % the backgroud noise level

dI = zeros(81,81,framNum);
parfor ii = 1:framNum % Parallel Calculation
    img = imStack(:,:,ii);
    fit_result = GaussianFitting2d(img);% fit_result = [A,x0,y0,s,z0,Rsquare]
    A = fit_result(1);
    s = fit_result(4);
    N = 2*pi*A*s^2/g;
    V = s^2/N*(16/9+8*pi*s^2*b^2/N);
    dI(:,:,ii) =  A*exp(-((idy'-fit_result(3)).^2 + (idx-fit_result(2)).^2) / (4*V));
end

I = zeros(81,81);
for ii = 1:framNum
    I(:,:) = I(:,:) + dI(:,:,ii);
end

figure(4);
imagesc(idx,idy,I);
title('PALM Reconstruction');