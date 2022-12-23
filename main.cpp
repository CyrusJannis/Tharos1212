int system(const char *command) {
    int response = system(command);
    cout << response << endl;
}
#include "../../../pchdef.h"
#include "../../playerbot.h"
#include "../../RandomPlayerbotFactory.h"
#include "../generic.h"

using namespace ai;

class GenericActionNodeFactory : public NamedObjectFactory<ActionNode>
{
public:
    GenericActionNodeFactory()
    {
        creators["melee"]
