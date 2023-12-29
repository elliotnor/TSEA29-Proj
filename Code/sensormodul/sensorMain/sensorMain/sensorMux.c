#include "sensorMux.h"


volatile uint8_t sensorCntr;


// Main-loop sequentially fetches data from ADC ports 0-3 and updates respectively
uint8_t getSensorData() {
	
	switch(sensorCntr) {
	
		case 0: // Sensor front
			return getFrontDistance();
		break;
			
		case 1: // Sensor right
			return getRightDistance();
		break;

		case 2: // Sensor left
			return getLeftDistance();
		break;
			
		case 3: // Gyro
			return getGyroData();
		break;
		
		case 4: // Odometer
			return getOdometerData();
		break;
		
	}
	return -1;
}