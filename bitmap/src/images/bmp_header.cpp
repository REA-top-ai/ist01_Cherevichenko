#include "../../include/images/bmp_header.h"
#include "../../include/file_loader.h"
#include "../../include/errors.h"

#include <cassert>
#include <stdexcept>

BMP_header::BMP_header(const char* path) {
    static_assert(sizeof(BMP_header) == 54, "BMP_header struct size is not 54 bytes");
    assert(sizeof(path) > 0);
    bool loaded = load(path);
    if (!loaded) {throw std::runtime_error(ERR_CANT_OPEN_FILE);}

    if (!is_BMP()) throw std::runtime_error(ERR_CANT_READ_IMAGE);
}

bool BMP_header::load(const char* path) {
    return load_file_bytes(path, reinterpret_cast<unsigned char*>(this), sizeof(BMP_header));
}

bool BMP_header::is_BMP() const {
    return (sign[0] == 'B' && sign[1] == 'M');
}

bool BMP_header::is_supported_bit_count() const {
    return (bit_count == 24 || bit_count == 16);
}

bool BMP_header::is_supported_compression() const {
    return (bit_count == 24 || (bit_count == 16 && compression == 3));
}
