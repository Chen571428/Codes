function [fitresult] = GaussianFitting2d(fit_img)
%{
2d Gaussian fitting for a single molecular image.
usage: fit_result = GaussianFitting2d(img).
OutPut:
    fit_result = [A,centroid_x0,centroid_y0, standar deviation s,z0,Rsquare];
Author: Riwang Chen <chenriwang@pku.edu.cn>
%}

%% prepare data
sz = size(fit_img);
x = 1:sz(2);
y = 1:sz(1);
x = x - 0.5;
y = y - 0.5;
[X,Y] = meshgrid(x,y);
[xData, yData, zData] = prepareSurfaceData( X, Y, fit_img );

%% Set up fittype and options.
formula = 'z0 + amp*exp(-(x-x0).^2/(2*sigma^2)-(y-y0).^2/(2*sigma^2))';
ft = fittype(formula, 'independent', {'x', 'y'}, 'dependent', 'z' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Algorithm = 'Levenberg-Marquardt';
opts.Display = 'Off';
amp_int = max(fit_img(:));
min_value = min(fit_img(:));
[y0,x0] = find(fit_img == amp_int);
opts.StartPoint = [amp_int-min_value 1 x0(1) y0(1) min_value];


% Fit model to data.
[ft, gof] = fit([xData, yData], zData, ft, opts);

fitresult = [ft.amp,ft.x0,ft.y0,ft.sigma,ft.z0,gof.rsquare];
end
