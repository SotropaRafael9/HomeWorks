#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
using namespace std;

int SortedMap::primaryHash(TKey key) const
{
	return key % capacity;
}

int SortedMap::secondaryHash(TKey key) const
{

	int step = key % (capacity - 1);
	return step;
	
}

SortedMap::SortedMap(Relation r) {
	//TODO - Implementation
	

	capacity = 10;
	this->length = 0;
	hashtable = new TElem[capacity];
	sortedArray = new TElem[capacity];
	for (int i = 0; i < capacity; i++)
	{
		hashtable[i] = NULL_TPAIR;
		sortedArray[i] = NULL_TPAIR;
	}
	relation = r;

}

TValue SortedMap::add(TKey k, TValue v) {
	//TODO - Implementation

	



}

TValue SortedMap::search(TKey k) const {
	//TODO - Implementation

	int index = primaryHash(k);
	TElem a = NULL_TPAIR;
	while (hashtable[index] != a && hashtable[index].first != k)
	{
		index = secondaryHash(index);
	}
	if (hashtable[index] == a)
		return NULL_TVALUE;
	else
		return hashtable[index].second;


}

TValue SortedMap::remove(TKey k) {
	//TODO - Implementation
	//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
	int index = primaryHash(k);
	int a = NULL_TVALUE;
	while (hashtable[index] != a && hashtable[index].first != k)
	{
		index = secondaryHash(index);
	}
	if (hashtable[index] == a)
		return NULL_TVALUE;
	else
	{
		TValue oldValue = hashtable[index].second;
		hashtable[index] = NULL_TPAIR;
		sortedArray[index] = NULL_TPAIR;
		length--;
		return oldValue;
	}
}

void SortedMap::resize()
{

	TElem* newHashtable = new TElem[capacity * 2];
	TElem* newSortedArray = new TElem[capacity * 2];
	for (int i = 0; i < capacity * 2; i++)
	{
		newHashtable[i] = NULL_TPAIR;
		newSortedArray[i] = NULL_TPAIR;
	}
	for (int i = 0; i < capacity; i++)
	{
		if (hashtable[i] != NULL_TPAIR)
		{
			int index = primaryHash(hashtable[i].first);
			while (newHashtable[index] != NULL_TPAIR)
			{
				index = secondaryHash(index);
			}
			newHashtable[index] = hashtable[i];
			newSortedArray[index] = hashtable[i];
		}
	}
	delete[] hashtable;
	delete[] sortedArray;
	hashtable = newHashtable;
	sortedArray = newSortedArray;
	capacity *= 2;
	

	
}

int SortedMap::size() const {
	//TODO - Implementation

	return this->length;
}

bool SortedMap::isEmpty() const {
	//TODO - Implementation
	return length == 0;
}

SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}

SortedMap::~SortedMap() {
	//TODO - Implementation


}
