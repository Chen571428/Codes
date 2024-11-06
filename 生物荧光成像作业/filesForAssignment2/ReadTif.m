function imgs = ReadTif(filename)
%{
read .tif files with Tiff class.
usage: imgs = ReadTif('xxxx.tif').
Output: the image stack represented by a 3d matrix @imgs
Author: Riwang Chen <chenriwang@pku.edu.cn>
%}

warning off;
t = Tiff(filename,'r');
info = imfinfo(filename);
t.setDirectory(1);
num_images = numel(info);
testreadx=info(1).Height;
testready=info(1).Width;

imgs = zeros(testreadx,testready,num_images);
for k = 1:num_images-1
    imgs(:,:,k)=t.read();
    t.nextDirectory();
end
imgs(:,:,num_images)=t.read();
t.close();
warning on;
end
