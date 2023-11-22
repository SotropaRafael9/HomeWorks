#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
	//TODO - Implementation
	// In  the constructor of the iterator create a sorted array of the elements and use it for iterating.


	for (int i = 0; i < map.capacity; i++)
	{
		if (map.sorted[i] != NULL_TPAIR)
			sortedArray.push_back(map.sorted[i]);
	}
	currentElement = 0;

}

SMIterator::~SMIterator()
{
	
}

void SMIterator::first(){
	//TODO - Implementation
	currentElement = 0;



}

void SMIterator::next(){
	//TODO - Implementation
	
	currentElement++;

}

bool SMIterator::valid() const{
	//TODO - Implementation
	return currentElement < sortedArray.size();
}

TElem SMIterator::getCurrent() const{
	//TODO - Implementation
	if (valid())
		return sortedArray[currentElement];
	else
		throw exception("Invalid iterator !");
	

}


