
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t cntr;
volatile uint8_t data;

void initI2C(void);

void TWILoadData(uint8_t cntr);

void dataReceived(void);

void enable_pullups(void);