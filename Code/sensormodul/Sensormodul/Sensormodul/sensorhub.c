/*

Created: 2023-11-16
Initializes all sensors and configures the ADC. Contains all functions for fetching data from sensors. 
Does all math.

*/

#include "sensorhub.h"

uint8_t gyroData;
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
	gyroData = readGyro();
	return gyroData;
}

/* Gets side + forward facing sensor-data from ADC. */
uint8_t getRightDistance() {
	rightDistance = rightDistanceCm();
	return rightDistance;
}

uint8_t getLeftDistance() {
	leftDistance = leftDistanceCm();
	return leftDistance;
	
}

uint8_t getFwdDistance() {
	fwdDistance = fwdDistanceCm();
	return fwdDistance;
}