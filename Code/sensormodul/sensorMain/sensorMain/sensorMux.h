#include <avr/io.h>
#include "odometer.h"
#include "sensorhub.h"


extern volatile uint8_t sensorCntr;



/* Main-loop sequentially fetches data from ADC ports 0-3 and updates respectively */
uint8_t getSensorData();

#endif