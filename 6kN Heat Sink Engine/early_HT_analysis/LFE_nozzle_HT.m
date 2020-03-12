% LFE HT at nozzle
clc, clear, close all
% MATERIAL PROPERTIES - from fundamentals of heat transfer 7th

% !!! next time make a material properties matrix and save a lot of typing

% 304 SS
Tm_304 = 1670; % melting point K
rho_304 = 7900; % density kg/m^3
% at 1000K
k_304 = 25.4; % thermal conductivity W/(m*k)
cp_304 = 611; % specific heat capacity J/(kg*K)
a_304 = k_304/(rho_304*cp_304); % thermal diffusivity m^2/s

% Al 2024-T6 (closest thing to 6061)
Tm_2024 = 775; % melting point K
rho_2024 = 2770; % density kg/m^3
% at 600K
k_2024 = 186; % thermal conductivity W/(m*k)
cp_2024 = 1042; % specific heat capacity J/(kg*K)
a_2024 = k_2024/(rho_2024*cp_2024); % thermal diffusivity m^2/s

% OTHER CONSTANTS
hg = 10e3; % nozzle convective HT coefficient, from 2019 LFE team W/(m^2*K)
Tg = 3500; % gas temp at nozzle K
rt = 24e-3; % throat radius meters
ro = 76.2e-3; % outer radius meters
T0 = 200; % initial pre-chilled nozzle temp (conservative?) Kelvin

% DOING IT AS A STUPID 1-D WALL (NOT CYLINDRICAL!)
L = ro - rt; % wall thickness
n = 20; % 100 nodes
dx = L/(n-1);
dt = .005; % try different stuff for time step
t_end = 5; % end time in seconds

Fo_304 = a_304*dt/dx^2; % compute Fo and Bi for materials
Bi_304 = hg*dx/k_304;
Fo_2024 = a_2024*dt/dx^2;
Bi_2024 = hg*dx/k_2024;

% initialize spatial matrix to initial temp
Temp = zeros(1,n);
Temp(1:end) = T0;

% could add hg calculation into loop

% 2024-T6 Aluminum
for ii = 1:(t_end)/dt-1
    % gas-side surface node
    newTemp = zeros(1,n);
    newTemp(1) = 2*Fo_2024*(Temp(ii,2)+Bi_2024*Tg)+...
        (1-2*Fo_2024-2*Bi_2024*Fo_2024)*Temp(ii,1);
    % interior nodes
    for jj = 2:n-1
        newTemp(jj) = Fo_2024*(Temp(ii,jj+1)+Temp(ii,jj-1))+...
            (1-2*Fo_2024)*Temp(ii,jj);
    end
    % node n
    newTemp(n) = a_2024*dt/(2*dx)*(Temp(ii,n)-Temp(ii,n-1))+...
        Temp(ii,n);
    % append newTemp
    Temp = [Temp;newTemp];
end

times = [.1 .2 .5 .8 1 1.5 2 2.5 3 3.5 4 4.5 5];
time_ind = times/dt;
wall = linspace(0,L*1e3,n);
figure
hold on

for ii = 1:length(time_ind)
    plot(wall,Temp(time_ind(ii),:))
end
melt_2024 = zeros(1,n);
melt_2024(:) = Tm_2024;
plot(wall,melt_2024,'k')
legend
grid on
ylabel('Temp (K)'),xlabel('Distance from nozzle surface (mm)')
title('2024-T6 Aluminum')
str = string(times);
lgd = legend(str,'melting point');
title(lgd,'time (s)')

% initialize spatial matrix to initial temp
Temp = zeros(1,n);
Temp(1:end) = T0;
% 304 SS
for ii = 1:(t_end)/dt-1
    % gas-side surface node
    newTemp = zeros(1,n);
    newTemp(1) = 2*Fo_304*(Temp(ii,2)+Bi_304*Tg)+...
        (1-2*Fo_304-2*Bi_304*Fo_304)*Temp(ii,1);
    % interior nodes
    for jj = 2:n-1
        newTemp(jj) = Fo_304*(Temp(ii,jj+1)+Temp(ii,jj-1))+...
            (1-2*Fo_304)*Temp(ii,jj);
    end
    % node n
    newTemp(n) = a_304*dt/(2*dx)*(Temp(ii,n)-Temp(ii,n-1))+...
        Temp(ii,n);
    % append newTemp
    Temp = [Temp;newTemp];
end

times = [.1 .2 .5 .8 1 1.5 2 2.5 3 3.5 4 4.5 5];
time_ind = times/dt;
wall = linspace(0,L*1e3,n);
figure
hold on

for ii = 1:length(time_ind)
    plot(wall,Temp(time_ind(ii),:))
end
melt_304 = zeros(1,n);
melt_304(:) = Tm_304;
plot(wall,melt_304,'k')
legend
grid on
ylabel('Temp (K)'),xlabel('Distance from nozzle surface (mm)')
title('304 Stainless Steel')
str = string(times);
lgd = legend(str,'melting point');
title(lgd,'time (s)')

