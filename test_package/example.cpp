#include <iostream>

#include "LuaIntf/LuaIntf.h"

int main() {
    using LuaIntf::LuaState;
    LuaState s = LuaState::newState();
    return 0;
}
