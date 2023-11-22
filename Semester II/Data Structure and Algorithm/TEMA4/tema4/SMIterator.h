#pragma once
#include "SortedMap.h"
#include <vector>

//DO NOT CHANGE THIS PART
class SMIterator{
	friend class SortedMap;
private:
	const SortedMap& map;
	SMIterator(const SortedMap& mapionar);

	//TODO - Representation
	// In  the constructor of the iterator create a sorted array of the elements and use it for iterating.
	
	std::vector<TElem> sortedArray;
	int currentElement;

public:
	~SMIterator();

	void first();
	void next();
	bool valid() const;
    TElem getCurrent() const;
};

