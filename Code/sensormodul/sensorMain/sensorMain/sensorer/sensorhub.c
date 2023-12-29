/*

Created: 2023-11-16
Initializes all sensors and configures the ADC. Contains all functions for fetching data from sensors. 
Does all math.

*/

#include "sensorhub.h"

uint8_t GYRO_DATA;
uint8_t rightDistance;
uint8_t leftDistance;
uint8_t fwdDistance;

void initSensors() {
	/* Initialize Gyroscope*/
	initGyro();

	/* Initialize IR-Sensors (distance) */
	// initDistance();

	/* Initialize the AD Converter */
	initADC();

}

/* Gets the gyro-data from the ADC */
uint8_t getGyroData() {
	GYRO_DATA = readGyro();
	return GYRO_DATA;
}

/* Gets side + forward facing sensor-data from ADC. */
uint8_t getRightDistance() {
	rightDistance = readRightData();
	return rightDistance;
}

uint8_t getLeftDistance() {
	leftDistance = readLeftData();
	return leftDistance;
	
}

uint8_t getFrontDistance() {
	fwdDistance = readFwdData();
	return fwdDistance;
}