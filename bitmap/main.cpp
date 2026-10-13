#include <iostream>
#include <fstream>
#include <cmath>

#define ERR_IF_FALSE(check, err_message, arg) if (!(check)) {std::cerr << err_message << arg << std::endl; return 1;}
constexpr auto ERR_CANT_OPEN_FILE{"File can't be open: "};
constexpr auto ERR_IS_NOT_BMP{"File is not BMP: "};
constexpr auto ERR_UNSUPPORTED_BIT_COUNT{"Unsupported bits per pixel: "};
constexpr auto ERR_CANT_READ_IMAGE{"Can't read image data: "};
constexpr auto ERR_UNSUPPORTED_COMPRESSION{"Unsupported compression: "};

static bool load_file_bytes(const char* path, unsigned char* buffer, const unsigned int size, const unsigned int offset = 0) {
    std::ifstream file(path, std::ios::binary);
    if (!file) { return false; }
    file.seekg(offset);
    file.read(reinterpret_cast<char*>(buffer), size);
    return true;
}

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

        bool load(const char* path) {
            return load_file_bytes(path, reinterpret_cast<unsigned char*>(this), sizeof(BMP_header));
        }

        bool is_BMP() const {
            return (sign[0] == 'B' && sign[1] == 'M');
        }

        bool is_supported_bit_count() const {
            return (bit_count == 24 || bit_count == 16);
        }

        bool is_supported_compression() const {
            return (bit_count == 24 || (bit_count == 16 && compression == 3));
        }
};
#pragma pack(pop)

#pragma pack(push, 1)
class Pixel {
    public:
        unsigned char B;
        unsigned char G;
        unsigned char R;

        void print_pixel() const {
            std::cout << "R: " << static_cast<int>(R) << " G: " << static_cast<int>(G) << " B: " << static_cast<int>(B);
        }
};
#pragma pack(pop)

class Bitmap {
    public:
        Bitmap(BMP_header headers) {
            this->headers = headers;
            this->pixels = new unsigned char[headers.image_size];
        }

        bool load(const char* path) {
            return load_file_bytes(path, pixels, headers.image_size, headers.data_offset);
        }

        Pixel get_pixel(unsigned int x, unsigned int y) const {
            return to_pixel(get_pixel_address(x, y));
        }

        ~Bitmap() {
            delete[] pixels;
        }

    private:
        BMP_header headers;
        unsigned char* pixels;

        const unsigned char* get_pixel_address(unsigned int x, unsigned int y) const {
            unsigned int row = headers.height - 1 - y;
            return pixels + (row * headers.width + x) * (headers.bit_count / 8);
            }

        Pixel to_pixel(const unsigned char* pixel) const {
            if (headers.bit_count == 16) {
                return pixel_from_16bit(pixel);
            }

            return *reinterpret_cast<const Pixel*>(pixel);
            }

        enum pixel_color{r, g, b};
        static unsigned char recover_16b_value (unsigned char subpixel, pixel_color color) {
            switch (color) {
                case r:
                    return subpixel * (pow(2, 8) - 1) / (pow(2, 5) - 1);
                    break;
                case g:
                    return subpixel * (pow(2, 8) - 1) / (pow(2, 6) - 1);
                    break;
                case b:
                    return subpixel * (pow(2, 8) - 1) / (pow(2, 5) - 1);
                    break;
            }

                return 0;
            }

        static Pixel pixel_from_16bit(const unsigned char* pixel) {
            const unsigned short value = *reinterpret_cast<const unsigned short*>(pixel);

            constexpr unsigned short b_16bit_mask = 0B0000000000011111;
            constexpr unsigned short g_16bit_mask = 0B0000011111100000;
            constexpr unsigned short r_16bit_mask = 0B1111100000000000;

            const unsigned char R = recover_16b_value((value & r_16bit_mask) >> 11, r);
            const unsigned char G = recover_16b_value((value & g_16bit_mask) >> 5, g);
            const unsigned char B = recover_16b_value(value & b_16bit_mask, b);

            return Pixel{B, G, R};
        }
};

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "../Rufous-Hummingbird_16.bmp";

    BMP_header headers;
    ERR_IF_FALSE(headers.load(path), ERR_CANT_OPEN_FILE, path);
    ERR_IF_FALSE(headers.is_BMP(), ERR_IS_NOT_BMP, path);
    ERR_IF_FALSE(headers.is_supported_bit_count(), ERR_UNSUPPORTED_BIT_COUNT, headers.bit_count);
    ERR_IF_FALSE(headers.is_supported_compression(), ERR_UNSUPPORTED_COMPRESSION, headers.compression);

    Bitmap image(headers);
    ERR_IF_FALSE(image.load(path), ERR_CANT_READ_IMAGE, path);

    unsigned int last_x = headers.width - 1;
    unsigned int last_y = headers.height - 1;
    Pixel left_up = image.get_pixel(0, 0);
    Pixel right_up = image.get_pixel(last_x, 0);
    Pixel left_down = image.get_pixel(0, last_y);
    Pixel right_down = image.get_pixel(last_x, last_y);

    left_up.print_pixel(); std::cout << "   ";
    right_up.print_pixel(); std::cout << std::endl;
    left_down.print_pixel(); std::cout << "    ";
    right_down.print_pixel(); std::cout << std::endl;
}