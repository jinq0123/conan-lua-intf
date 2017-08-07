from conans import ConanFile

class LuaintfConan(ConanFile):
    name = "lua-intf"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/jinq0123/conan-lua-intf"
    description = "A binding between C++11 and Lua language"
    # No settings/options are necessary, this is header only

    def source(self):
        self.run("git clone --depth=1 https://github.com/SteveKChiu/lua-intf.git")

    def package(self):
        self.copy("*", dst="include", src="lua-intf")

    def package_id(self):
        self.info.header_only()
