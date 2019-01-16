load('humid.csv');
load('light.csv');
load('temp.csv');

x=1:1:497;

% Plot humid
figure(1);
plot(x,humid);
axis([0 400 0 100]);
xlabel('Sample no.')
ylabel('Humidity (%)')
% Plot light
figure(2);
plot(x,light);
axis([0 400 0 150]);
xlabel('Sample no.')
ylabel('Light (lux)')
% Plot temp
figure(3);
plot(x,temp);
axis([0 400 12 20]);
xlabel('Sample no.')
ylabel('Temperature (C)')