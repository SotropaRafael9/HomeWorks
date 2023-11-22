#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
	//TODO - Implementation
	this->current = this->map.head;
}


void MapIterator::first() {
	//TODO - Implementation
	this->current = this->map.head;
}


void MapIterator::next() {
	//TODO - Implementation
	if (!this->valid())
		throw exception();
	this->current = this->map.Nodes[current].next;
}


TElem MapIterator::getCurrent(){
	//TODO - Implementation
	if (!this->valid())
		throw exception();

	return this->map.Nodes[current].element;
}


bool MapIterator::valid() const {
	//TODO - Implementation
	if (this->current == -1)
		return false;
	return true;
}

void MapIterator::jumpForward(int k)
{
	if (k <= 0)
		throw exception();
	if (!this->valid())
		throw exception();
	int i = 0;
	while (i < k && this->current != -1)
	{
		this->current = this->map.Nodes[current].next;
		i++;
	}
}





