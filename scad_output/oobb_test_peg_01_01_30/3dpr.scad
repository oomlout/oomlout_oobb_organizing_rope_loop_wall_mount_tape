$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -30.0000000000]) {
			cylinder(h = 30, r = 7);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 13);
		}
	}
	union() {
		#translate(v = [0, 0, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
	}
}