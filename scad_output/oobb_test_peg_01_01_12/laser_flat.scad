$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -4.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 7);
						}
						translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6, r = 13);
						}
					}
					union() {
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 4.0000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 24, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -1.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 7);
						}
						translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6, r = 13);
						}
					}
					union() {
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 4.0000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 48, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 1.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 7);
						}
						translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6, r = 13);
						}
					}
					union() {
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 4.0000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 72, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 4.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 7);
						}
						translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6, r = 13);
						}
					}
					union() {
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 4.0000000000);
						}
					}
				}
			}
		}
	}
}