import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "test"

        kwargs["save_type"] = "none"
        #kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "test" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 3
        p3["height"] = 6
        p3["thickness"] = 6
        part["kwargs"] = p3
        
        part["name"] = "base"
        parts.append(part)


    part = copy.deepcopy(part_default)
    p3 = copy.deepcopy(kwargs)
    p3["thickness"] = 4
    p3["width"] = 1
    p3["height"] = 1
    
    p3["thickness"] = 12
    p3["flange_extra"] = 12
    p3["flange_depth"] = 6
    p3["screw_diameter"] = "m8"    
    part["kwargs"] = p3
    part["name"] = "peg"
    parts.append(part)


    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[1] += -7.5
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add plate for rope
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth+15
    p3["height"] = 2
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[1] += -(height/2 * 15) + 15/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["height"] = height-1
    p3["holes"] = "single"
    locs = []
    locs.append([1,5])
    locs.append([3,5])
    p3["location"] = locs
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add 27 mm diameter hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius"] = 13.5
    #p3["m"] = "#"
    d = 20
    p3["depth"] = d
    pos1 = copy.deepcopy(pos)    
    pos1[1] += 6
    #clearance hole
    pos2 = copy.deepcopy(pos)
    pos2[1] += -22.5
    pos2[2] += depth    
    poss = []
    poss.append(pos1)
    poss.append(pos2)
    p3["pos"] = poss
    oobb_base.append_full(thing,**p3)

    #add 15 mm diameter slot
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_slot"
    p3["radius"] = 7.5
    p3["width"] = 60-15
    p3["depth"] = depth
    #p3["m"] = "#"
    p3["zz"] = "top"
    rot1 = copy.deepcopy(rot)
    rot1[2] = 90
    p3["rot"] = rot1
    pos1 = copy.deepcopy(pos)    
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add m6 hole for rope
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m8"
    d = (width * 15) - 1
    p3["depth"] = d
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[0] += -d/2
    pos1[1] += -((height-1)/2) * 15 
    pos1[2] += depth + 15/2
    p3["pos"] = pos1
    rot1 = copy.deepcopy(rot)
    rot1[1] = 90
    p3["rot"] = rot1
    p3["zz"] = "middle"
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_peg(thing, **kwargs):
    name = kwargs.get("type", "default")
    if True:
        depth = kwargs.get("thickness", 4)
        radius = kwargs.get("radius", 10)
        prepare_print = kwargs.get("prepare_print", False)
        screw_diameter = kwargs.get("screw_diameter", "m4_screw_wood")
        #
        flange_extra = kwargs.get("flange_extra", 0)
        flange_depth = kwargs.get("flange_depth", 0)
        flat_length = kwargs.get("flat_length", 0)
        multi_hole = kwargs.get("multi_hole", 1)



        pos = kwargs.get("pos", [0, 0, 0])
        #pos = copy.deepcopy(pos)
        #pos[2] += -20

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"    
        p3["depth"] = depth
        p3["radius"] = 7
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)
        #add flange if flange extra is set
        if flange_extra > 0:            
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"oobb_cylinder"    
            p3["depth"] = flange_depth
            p3["radius"] = 13
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)
    


        #add holes
        if True:
            if multi_hole == 1:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_hole"    
                #p3["depth"] = depth
                p3["radius_name"] = screw_diameter
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)
            


        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 50
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)


###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)