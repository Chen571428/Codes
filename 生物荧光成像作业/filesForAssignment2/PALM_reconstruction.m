% this script is to simulate the reconstruction principle of STORM
% Author: Chen571428 2400934013 20241105

close all;
clear;

imStack = ReadTif('TestPALM.tif'); % load images 
framNum = size(imStack,3);% the number of the input images

idx = 5.5:0.05:9.5;
idy = 6.5:0.05:10.5;

[X,Y] = meshgrid(idx,idy);
% params = [A,x0,y0,s^2]
imgGaussian = @(params) params(1)*exp(-0.5*((X-params(2)).^2+(Y-params(3)).^2)/params(4));

g = 1; % the overall gain of the imaging system
b = 5/g; % the backgroud noise level
zPerFram = zeros(framNum,size(X,1),size(Y,1));
parfor ii = 1:framNum % Parallel Calculation 
% for ii = 1:framNum
    img = imStack(:,:,ii);
    %fit_result = [A,x0,y0,s,z0,Rsquare]
    fit_result = GaussianFitting2d(img);
    A = fit_result(1);
    s = fit_result(4);
    N = 2*pi*A*s^2/g;

    varX0 = s^2 / N * (16 / 9 + 8*pi*s^2*b^2 / N);
    varY0 = varX0;
    sigmaXY = sqrt(varX0 + varY0);

    x0(ii) = fit_result(2);
    y0(ii) = fit_result(3);

    
    for xi = 1:81
        for yi = 1:81
            zPerFram(ii,xi,yi) = A * exp (- ((((idx(xi) - x0(ii))^2) / (2*sigmaXY^2)) + (((idy(yi) - y0(ii))^2) / (2*sigmaXY^2)) ));
        end
    end

end
z0 = zeros(81,81);

for ii = 1:framNum
    for xi = 1:81
        for yi = 1:81
            z0(yi,xi) = z0(yi,xi) + zPerFram(ii,xi,yi);
        end
    end
end
dpx = ["" ""];
dpy = ["" ""];

for i = 1:81
    if mod(i,10) == 1
        dpx(i) = num2str(idx(i),'%.1f');
        dpy(i) = num2str(idy(i),'%.1f');
    else 
        dpx(i) = ' ';
        dpy(i) = ' ';
    end
end

% figure;
% heatmap(idx,idy,z0,"Colormap",hot,"GridVisible","off","Title","PALM Reconstruction","XDisplayLabels",dpx,"YDisplayLabels",dpy)
figure("Name","PALM Reconstruction")
imagesc(z0,"XData",idx,"YData",idy)
title("PALM Reconstruction")
colormap('hot')
colorbar
xlim("auto")

% set(gca,'xtick',idx)
% set(gca,'xticklabel',dpx)
% set(gca,'ytick',idy)
% set(gca,'yticklabel',dpy)



% plot(x0,y0,'.');
% title('STORM Reconstruction');
