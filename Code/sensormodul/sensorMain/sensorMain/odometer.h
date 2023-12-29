
#ifndef ODOMETER_H_
#define ODOMETER_H_

#include <avr/io.h>

volatile uint8_t odometer_cntr;


//L?ngd p? pinne = 5,8*pi/40 cm = 0.4555cm = 4.55mm
//Diameter 5,8cm
//Antal gropar 40


void setup_odometer();

void reset_odometer_cntr();


void odometerInterrupt();

uint8_t getOdometerData();

#endif