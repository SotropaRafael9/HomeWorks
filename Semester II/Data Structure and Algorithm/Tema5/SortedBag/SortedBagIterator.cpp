#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	// //TODO - Implementation
	// initializeStack();
	// first();
	curr = 0;
	for(int i = 0; i < bag.elements.size(); i++)
		for(int j = 0; j < bag.elements[i].frequency; j++)
			elements.push_back(bag.elements[i].element);
	
	 for (int i = 0; i < elements.size() - 1; i++)
        for (int j = i + 1; j < elements.size(); j++)
            if (!bag.relation(elements[i], elements[j]))
                std::swap(elements[i], elements[j]);

}


// void SortedBagIterator::initializeStack()
// {
// 	stackSize = bag.size();
// 	stack = new int[stackSize];
// }

// int SortedBagIterator::getMinimumNodeIndex(int startIndex) const
// {
// 	int currentNode = startIndex;
// 	while (bag.elements[currentNode].leftChildIndex != -1)
// 		currentNode = bag.elements[currentNode].leftChildIndex;

// 	return currentNode;
// }

// void SortedBagIterator::goToNextNode()
// {
// 	if (occurrencesLeft > 1)
// 	{
// 		occurrencesLeft--;
// 		return;
// 	}
// 	else
// 	{
// 		if (bag.elements[currentNodeIndex].rightChildIndex != -1)
// 		{
// 			currentNodeIndex = getMinimumNodeIndex(bag.elements[currentNodeIndex].rightChildIndex);
// 			currentFrequency = bag.elements[currentNodeIndex].frequency;
// 			occurrencesLeft = currentFrequency;
// 		}
// 		else
// 		{
// 			int parent = stack[stackSize - 1];
// 			stackSize--;
// 			while (parent != -1 && bag.elements[parent].rightChildIndex == currentNodeIndex)
// 			{
// 				currentNodeIndex = parent;
// 				parent = stack[stackSize - 1];
// 				stackSize--;
// 			}
// 			if (parent == -1)
// 				traversalIndex = -1;
// 			else
// 			{
// 				currentNodeIndex = parent;
// 				currentFrequency = bag.elements[currentNodeIndex].frequency;
// 				occurrencesLeft = currentFrequency;
// 			}
// 		}
// 	}
// }

TComp SortedBagIterator::getCurrent() {
	if(valid())
		return elements[curr];
	else
		throw exception();
}

bool SortedBagIterator::valid() {
	return curr < elements.size();
}

void SortedBagIterator::next() {
	if(valid())
		curr++;
	else
		throw exception();
}

void SortedBagIterator::first() {
	curr = 0;
}

