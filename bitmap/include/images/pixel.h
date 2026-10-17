#pragma once

#pragma pack(push, 1)
class Pixel {
    public:
        unsigned char B;
        unsigned char G;
        unsigned char R;
        unsigned char Y;

        Pixel(unsigned char b, unsigned char g, unsigned char r);
        void print_pixel() const;
};
#pragma pack(pop)
