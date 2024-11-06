# ReadMe

For convenience, the photon coefficient $g$ is set to $1$ and the background noise level $\sigma$ is set to $5$.

Fitting model:
$$
f(\theta)=A e^{-\frac{(x-x_0)^2+(y-y_0)^2}{2s^2}} + z_0 \\
where \  \theta =(A,x_0,y_0,s,z_0)
$$
Fitting function and usage:

> fit_result = GaussianFitting2d(image);

The output parameter fit_result $=(A,x_0,y_0,s,z_0,RSquare)$.

Note: the photon number $N=2\pi As^2/g$





