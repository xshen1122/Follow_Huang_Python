mkdir resolution_32x32_m3u8
./realproducerhd -i xmen_2560x1440_60sec.mp4 -s 32x32 -hls_time 10 -avgrate 100k -b:a 32k /resolution_32x32_m3u8/resolution_32x32_m3u8.m3u8
mkdir resolution_80x60_m3u8
./realproducerhd -i xmen_2560x1440_60sec.mp4 -s 80x60 -hls_time 10 -avgrate 100k -b:a 32k /resolution_80x60_m3u8/resolution_80x60_m3u8.m3u8
mkdir resolution_60x80_m3u8
./realproducerhd -i xmen_2560x1440_60sec.mp4 -s 60x80 -hls_time 10 -avgrate 100k -b:a 32k /resolution_60x80_m3u8/resolution_60x80_m3u8.m3u8
mkdir resolution_160x90_m3u8
./realproducerhd -i xmen_2560x1440_60sec.mp4 -s 160x90 -hls_time 10 -avgrate 350k -b:a 64k /resolution_160x90_m3u8/resolution_160x90_m3u8.m3u8
mkdir resolution_90x160_m3u8
./realproducerhd -i xmen_2560x1440_60sec.mp4 -s 90x160 -hls_time 10 -avgrate 100k -b:a 32k /resolution_90x160_m3u8/resolution_90x160_m3u8.m3u8
