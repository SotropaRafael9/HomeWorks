#pragma once
#include "SortedBag.h"
#include <vector>
class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	const SortedBag& bag;
	SortedBagIterator(const SortedBag& b);
	

	// //TODO - Representation
	// int currentNodeIndex;  // Index of the current node in the array
	// int currentFrequency;  // Current frequency of the element
	// int occurrencesLeft;   // Number of occurrences left to iterate
	// int traversalIndex;    // Index used for traversal of the array
	// int stackSize;         // Size of the stack
	// int* stack;            // Stack to store the path to the current node

	// // Private methods
	// void initializeStack();
	// int getMinimumNodeIndex(int startIndex) const;
	// void goToNextNode();

	std::vector<TComp> elements;
	int curr;

	
	
public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();
};

