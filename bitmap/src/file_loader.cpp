#include "../include/file_loader.h"

#include <fstream>

bool load_file_bytes(const char* path, unsigned char* buffer, const unsigned int size, const unsigned int offset) {
    std::ifstream file(path, std::ios::binary);
    if (!file) { return false; }
    file.seekg(offset);
    file.read(reinterpret_cast<char*>(buffer), size);
    return true;
}
