$fn = 50;


difference() {
	union() {
		translate(v = [0, -7.5000000000, 0]) {
			hull() {
				translate(v = [-17.0000000000, 39.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [17.0000000000, 39.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-17.0000000000, -39.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [17.0000000000, -39.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
		translate(v = [0, -37.5000000000, 0]) {
			hull() {
				translate(v = [-17.0000000000, 9.5000000000, 0]) {
					cylinder(h = 21, r = 5);
				}
				translate(v = [17.0000000000, 9.5000000000, 0]) {
					cylinder(h = 21, r = 5);
				}
				translate(v = [-17.0000000000, -9.5000000000, 0]) {
					cylinder(h = 21, r = 5);
				}
				translate(v = [17.0000000000, -9.5000000000, 0]) {
					cylinder(h = 21, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 90]) {
				difference() {
					union() {
						hull() {
							translate(v = [22.5000000000, 0, 0]) {
								cylinder(h = 6, r = 7.5000000000, r1 = 7.5000000000, r2 = 7.5000000000);
							}
							translate(v = [-22.5000000000, 0, 0]) {
								cylinder(h = 6, r = 7.5000000000, r1 = 7.5000000000, r2 = 7.5000000000);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-15.0000000000, 30.0000000000, 0]) {
			cylinder(h = 6, r = 3.0000000000);
		}
		translate(v = [15.0000000000, 30.0000000000, 0]) {
			cylinder(h = 6, r = 3.0000000000);
		}
		translate(v = [0, 6, 0]) {
			cylinder(h = 20, r = 13.5000000000);
		}
		translate(v = [0, -22.5000000000, 6]) {
			cylinder(h = 20, r = 13.5000000000);
		}
		translate(v = [-22.0000000000, -37.5000000000, 13.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 44, r = 4.0000000000);
			}
		}
	}
}