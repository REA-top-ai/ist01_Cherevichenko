#pragma once

#pragma pack(push, 1)
class BMP_header {
    public:
        unsigned char sign[2];
        unsigned int file_size;
        unsigned int reserved;
        unsigned int data_offset;
        unsigned int info_header_size;
        unsigned int width;
        unsigned int height;
        unsigned short planes;
        unsigned short bit_count;
        unsigned int compression;
        unsigned int image_size;
        unsigned int x_pixels_per_m;
        unsigned int y_pixels_per_m;
        unsigned int colors_used;
        unsigned int color_important;

        BMP_header(const char* path);
        bool load(const char* path);
        bool is_BMP() const;
        bool is_supported_bit_count() const;
        bool is_supported_compression() const;
};
#pragma pack(pop)
