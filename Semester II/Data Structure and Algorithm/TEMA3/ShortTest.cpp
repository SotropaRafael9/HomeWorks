#include "ShortTest.h"
#include <assert.h>
#include <iostream>
#include "Map.h"
#include "MapIterator.h"


void testAll() { //call each function to see if it is implemented
	Map m;
	assert(m.isEmpty() == true);
	assert(m.size() == 0); //add elements
	assert(m.add(5,5)==NULL_TVALUE);
	assert(m.add(1,111)==NULL_TVALUE);
	assert(m.add(10,110)==NULL_TVALUE);
	assert(m.add(7,7)==NULL_TVALUE);
	assert(m.add(1,1)==111);
	assert(m.add(10,10)==110);
	assert(m.add(-3,-3)==NULL_TVALUE);
	assert(m.size() == 5);
	assert(m.search(10) == 10);
	assert(m.search(16) == NULL_TVALUE);
	assert(m.remove(1) == 1);
	assert(m.remove(6) == NULL_TVALUE);
	assert(m.size() == 4);


	TElem e;
	MapIterator id = m.iterator();
	id.first();
	int s1 = 0, s2 = 0;
	while (id.valid()) {
		e = id.getCurrent();
		s1 += e.first;
		s2 += e.second;
		id.next();
	}
	assert(s1 == 19);
	assert(s2 == 19);

	Map m_bonus;
	assert(m_bonus.add(5, 5) == NULL_TVALUE);
	assert(m_bonus.add(1, 111) == NULL_TVALUE);
	assert(m_bonus.add(10, 110) == NULL_TVALUE);
	assert(m_bonus.add(7, 7) == NULL_TVALUE);
	assert(m_bonus.add(1, 1) == 111);
	assert(m_bonus.add(10, 10) == 110);
	assert(m_bonus.add(-3, -3) == NULL_TVALUE);
	MapIterator id_bonus = m_bonus.iterator();
	id_bonus.first();
	id_bonus.jumpForward(2);
	assert(id_bonus.getCurrent() == TElem( 10,10 ));
	id_bonus.jumpForward(5);
	assert(!id_bonus.valid());
	try
	{
		id_bonus.jumpForward(1);
		assert(false);
	}
	catch (std::exception &) {
		assert(true);
	}

}


