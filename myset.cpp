#include <iostream>
#include <set>
#include <utility>
using namespace std;

int main()
{
	set<pair<string, int>> set = {
		{"A", 4}, {"B", 4}, {"C", 1}, {"A", 0}, {"B", 3}
	};

    if (set.find(make_pair("A",4)) == set.end()) {
        cout << "Absent";
    } else
        cout << "Present";

	for (auto const &p: set) {
		cout << p.first << " " << p.second << '\n';
	}

	return 0;
}
