clear;close all;
imStack = ReadTif('TestPALM.tif');
framNum = size(imStack,3);
width = size(imStack,2);
height = size(imStack,1);

Stacking = zeros(width,height);

for i  = 1:framNum
    imagesc(imStack(:,:,i));
    exportgraphics(gca,'eachGraph.gif','Append',true);
end
