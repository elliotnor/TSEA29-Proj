/*
 * Styrmodul.h
 *
 * Created: 2023-11-07 13:04:22
 */ 

#include <avr/io.h>
#include <util/delay.h>
#include <stdbool.h>

enum Direction {BACKWARD, FORWARD};
	
void pwm_init();

void set_direction(enum Direction dir);
	
void rotate_left();

void rotate_right();

void set_left_wheels(enum Direction dir);

void set_right_wheels(enum Direction dir);

void set_speed(uint8_t speed);

void stop();

void turn_right();

void turn_left();

void stop_turning();

void rotate_90_left();

void rotate_90_right();
	