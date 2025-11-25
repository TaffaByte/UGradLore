#ifndef q3_hotel_h
#define q3_hotel_h

#include <iostream>

class HotelRoom {
protected:
	int bedrooms;
	int bathrooms;
public:
	HotelRoom(int b, int ba)
		: bedrooms(b), bathrooms(ba) {}

	virtual ~HotelRoom() = default;

	virtual int get_price() const {
		return bedrooms * 100 + bathrooms * 50;
	}
};

class HotelApartment : public HotelRoom {
public:
	HotelApartment(int b, int ba)
		: HotelRoom(b, ba) {}

	int get_price() const override {
		return HotelRoom::get_price();
	}
};

#endif