import bpy  # type: ignore
import math
import os

# Metadati dell'addon
bl_info = {
    "name": "OW_AutoRigger",
    "author": "Bogus_Corp",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool",
    "description": "Rename, organize, and create a custom rig for OW characters",
    "category": "Object",
}

# Liste di nomi originali e nuovi nomi
Lista_nomi_originali = [
    "bone_005B",
    "bone_005A",
    "bone_0059",
    "bone_0055",
    "bone_0065",
    "bone_0064",
    "bone_0063",
    "bone_005F",
    "bone_0053",
    "bone_0002",
    "bone_0001",
    "bone_0000",
    "bone_0003",
    "bone_0011",
    "bone_0010",
    "bone_0005",
    "bone_0004",
    "bone_0052",
    "bone_002B",
    "bone_002A",
    "bone_0029",
    "bone_001F",
    "bone_001E",
    "bone_001D",
    "bone_0022",
    "bone_0021",
    "bone_0020",
    "bone_0028",
    "bone_0027",
    "bone_0026",
    "bone_0025",
    "bone_0024",
    "bone_0023",
    "bone_001C",
    "bone_000E",
    "bone_000D",
    "bone_0050",
    "bone_0049",
    "bone_0048",
    "bone_0047",
    "bone_003D",
    "bone_003C",
    "bone_003B",
    "bone_0040",
    "bone_003F",
    "bone_003E",
    "bone_0046",
    "bone_0045",
    "bone_0044",
    "bone_0043",
    "bone_0042",
    "bone_0041",
    "bone_003A",
    "bone_0037",
    "bone_0036",
    "bone_0035",
    "bone_03BC",  # "TAR-JAW",
    "bone_000B",  # "TAR-UPPER_JAW",
    "bone_03B9",  # "TAR-TONGUE-03",
    "bone_03BA",  # "TAR-TONGUE-02",
    "bone_03BB",  # "TAR-TONGUE-01",
    "bone_03B7",  # TAR-UPPER-TEETH"
    "bone_03B8",  #  "TAR-LOWER-TEETH",
    "bone_0397",  # TAR-UPPER-EYELID.L"
    "bone_039A",  # TAR-EYE.L
    "bone_0396",  # "TAR-INFERIOR-EYELID.L"
    "bone_0399",  # "TAR-UPPER-EYELID.R",
    "bone_039B",  # "TAR-EYE.R",
    "bone_0398",  # "TAR-INFERIOR-EYELID.R"
]
Lista_nuovi_nomi = [
    "TAR-TOE.L",
    "TAR-FOOT.L",
    "TAR-SHIN.L",
    "TAR-LEG.L",
    "TAR-TOE.R",
    "TAR-FOOT.R",
    "TAR-SHIN.R",
    "TAR-LEG.R",
    "TAR-HIPS",
    "TAR-BODY",
    "root",
    "TAR-ROOT",
    "TAR-UPPER BODY",
    "TAR-HEAD",
    "TAR-NECK",
    "TAR-CHEST",
    "TAR-SPINE",
    "TAR-SPINE-02",
    "TAR-FINGER-E-03.L",
    "TAR-FINGER-E-02.L",
    "TAR-FINGER-E-01.L",
    "TAR-FINGER-D-03.L",
    "TAR-FINGER-D-02.L",
    "TAR-FINGER-D-01.L",
    "TAR-FINGER-C-03.L",
    "TAR-FINGER-C-02.L",
    "TAR-FINGER-C-01.L",
    "TAR-FINGER-B-03.L",
    "TAR-FINGER-B-02.L",
    "TAR-FINGER-B-01.L",
    "TAR-FINGER-A-03.L",
    "TAR-FINGER-A-02.L",
    "TAR-FINGER-A-01.L",
    "TAR-HAND.L",
    "TAR-FOREARM.L",
    "TAR-ARM.L",
    "TAR-SHOULDER.L",
    "TAR-FINGER-E-03.R",
    "TAR-FINGER-E-02.R",
    "TAR-FINGER-E-01.R",
    "TAR-FINGER-D-03.R",
    "TAR-FINGER-D-02.R",
    "TAR-FINGER-D-01.R",
    "TAR-FINGER-C-03.R",
    "TAR-FINGER-C-02.R",
    "TAR-FINGER-C-01.R",
    "TAR-FINGER-B-03.R",
    "TAR-FINGER-B-02.R",
    "TAR-FINGER-B-01.R",
    "TAR-FINGER-A-03.R",
    "TAR-FINGER-A-02.R",
    "TAR-FINGER-A-01.R",
    "TAR-HAND.R",
    "TAR-FOREARM.R",
    "TAR-ARM.R",
    "TAR-SHOULDER.R",
    "TAR-JAW",
    "TAR-UPPER_JAW",
    "TAR-TONGUE-03",
    "TAR-TONGUE-02",
    "TAR-TONGUE-01",
    "TAR-UPPER-TEETH",
    "TAR-LOWER-TEETH",
    "TAR-UPPER-EYELID.L",
    "TAR-EYE.L",
    "TAR-INFERIOR-EYELID.L",
    "TAR-UPPER-EYELID.R",
    "TAR-EYE.R",
    "TAR-INFERIOR-EYELID.R",
]

Escludi_bones = [
    "TAR-JAW",
    "TAR-UPPER_JAW",
    "TAR-TONGUE-03",
    "TAR-UPPER-TEETH",
    "TAR-LOWER-TEETH",
    "TAR-UPPER-EYELID.L",
    "TAR-EYE.L",
    "TAR-INFERIOR-EYELID.L",
    "TAR-UPPER-EYELID.R",
    "TAR-EYE.R",
    "TAR-INFERIOR-EYELID.R",
    "TAR-HAND.R",
    "TAR-HAND.L",
    "TAR-BODY-ROOT",
    "TAR-UPPER BODY",
    "TAR-TOE.L",
    "TAR-TOE.R",
    "TAR-HIPS",
    "TAR-HEAD",
    "TAR-FINGER-E-03.L",
    "TAR-FINGER-D-03.L",
    "TAR-FINGER-C-03.L",
    "TAR-FINGER-B-03.L",
    "TAR-FINGER-A-03.L",
    "TAR-FINGER-E-03.R",
    "TAR-FINGER-D-03.R",
    "TAR-FINGER-C-03.R",
    "TAR-FINGER-B-03.R",
    "TAR-FINGER-A-03.R",
]

roll_degree_list = [
    -52.7657,
    178.663,
    185.725,
    185.725,
    8.7,
    175.5,
    185.725,
    185.725,
    180,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    140.574,
    -199.927,
    207.174,
    120.056,
    117.105,
    84.0826,
    102.754,
    99.4,
    66.5409,
    90.48,
    87.8414,
    49.9587,
    71.8036,
    75.634,
    43.2475,
    45.8728,
    53.3737,
    46.2262,
    0,
    140.574,
    -199.927,
    -199.927,
    -120.056,
    -117.105,
    -84.0826,
    -102.754,
    -99.4,
    -66.5409,
    -90.48,
    -87.8414,
    -49.9587,
    -71.8036,
    -75.634,
    -43.2475,
    -45.8728,
    -53.3737,
    -46.2262,
    0,
    0,
    0,
    180,
    0,
    0,
    0,
    0,
    0,
    0,
    180,
    180,
    0,
    180,
    180,
]


# Operatore per rinominare le ossa
class RENAME_BONES_OT_Rename(bpy.types.Operator):
    bl_idname = "object.rename_bones"
    bl_label = "Rename Bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        armature = context.active_object
        if armature and armature.type == "ARMATURE":
            for bone in armature.data.bones:
                if bone.name in Lista_nomi_originali:
                    index = Lista_nomi_originali.index(bone.name)
                    bone.name = Lista_nuovi_nomi[index]
            self.report({"INFO"}, "Nomi delle ossa aggiornati.")
        else:
            self.report({"WARNING"}, "Per favore, seleziona un'armatura.")
        return {"FINISHED"}


# Operatore per disporre le ossa
class ARRANGE_BONES_OT_Arrange(bpy.types.Operator):
    bl_idname = "object.arrange_bones"
    bl_label = "Arrange Armature"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        armature = context.active_object
        if armature and armature.type == "ARMATURE":
            with bpy.context.temp_override(object=armature):
                bpy.ops.object.mode_set(mode="EDIT")  # Passa in modalità Edit

                # Connessione delle ossa in sequenza
                prev_bone = None
                for bone_name in Lista_nuovi_nomi:
                    if prev_bone and not any(
                        excl in bone_name for excl in Escludi_bones
                    ):
                        bone = armature.data.edit_bones.get(bone_name)
                        if bone and prev_bone:
                            bone.tail = prev_bone.head  # Collegare le ossa
                    prev_bone = armature.data.edit_bones.get(bone_name)

                # Trasformazioni specifiche per le ossa escluse
                for bone_name in Escludi_bones:
                    bone = armature.data.edit_bones.get(bone_name)
                    if bone:
                        if bone_name == "TAR-HEAD":
                            bone.tail[2] += 0.2  # Sposta sull'asse Z
                        elif bone_name == "TAR-HIPS":
                            bone.tail[2] -= 0.3  # Sposta sull'asse Z
                        elif bone_name in ["TAR-TOE.L", "TAR-TOE.R"]:
                            bone.tail[1] -= 0.2  # Sposta sull'asse Y
                        elif bone_name == "TAR-HAND.R":
                            # Calcolo del punto medio per TAR-HAND.R
                            finger_b01_r = armature.data.edit_bones.get(
                                "TAR-FINGER-B-01.R"
                            )
                            finger_c01_r = armature.data.edit_bones.get(
                                "TAR-FINGER-C-01.R"
                            )
                            hand_r = armature.data.edit_bones.get("TAR-HAND.R")

                            if finger_b01_r and finger_c01_r and hand_r:
                                midpoint = (
                                    (
                                        finger_b01_r.head[0]
                                        + finger_c01_r.head[0]
                                        + hand_r.head[0]
                                    )
                                    / 3,
                                    (
                                        finger_b01_r.head[1]
                                        + finger_c01_r.head[1]
                                        + hand_r.head[1]
                                    )
                                    / 3,
                                    (
                                        finger_b01_r.head[2]
                                        + finger_c01_r.head[2]
                                        + hand_r.head[2]
                                    )
                                    / 3,
                                )
                                bone.tail = midpoint
                        elif bone_name == "TAR-HAND.L":
                            # Calcolo del punto medio per TAR-HAND.L
                            finger_b01_l = armature.data.edit_bones.get(
                                "TAR-FINGER-B-01.L"
                            )
                            finger_c01_l = armature.data.edit_bones.get(
                                "TAR-FINGER-C-01.L"
                            )
                            hand_l = armature.data.edit_bones.get("TAR-HAND.L")

                            if finger_b01_l and finger_c01_l and hand_l:
                                midpoint_l = (
                                    (
                                        finger_b01_l.head[0]
                                        + finger_c01_l.head[0]
                                        + hand_l.head[0]
                                    )
                                    / 3,
                                    (
                                        finger_b01_l.head[1]
                                        + finger_c01_l.head[1]
                                        + hand_l.head[1]
                                    )
                                    / 3,
                                    (
                                        finger_b01_l.head[2]
                                        + finger_c01_l.head[2]
                                        + hand_l.head[2]
                                    )
                                    / 3,
                                )
                                bone.tail = midpoint_l

                # Spostamento delle ossa "FINGER" con "03" nel nome lungo l'asse Z
                for bone in armature.data.edit_bones:
                    if "FINGER" in bone.name and "03" in bone.name:
                        bone.tail[2] -= 0.005  # Sposta sull'asse Z

                # Trasformazioni aggiuntive secondo le richieste
                transformations = {
                    "TAR-UPPER-EYELID.L": (0, 0, 0.006),
                    "TAR-UPPER-EYELID.R": (0, 0, 0.006),
                    "TAR-INFERIOR-EYELID.L": (0, 0, -0.006),
                    "TAR-INFERIOR-EYELID.R": (0, 0, -0.006),
                    "TAR-EYE.L": (0, -0.006, 0),
                    "TAR-EYE.R": (0, -0.006, 0),
                    "TAR-TONGUE-03": (0, -0.006, 0),
                    "root": (0, 0.5, -1.12951),
                    "TAR-UPPER-TEETH": (0, 0, 0.009),
                    "TAR-LOWER-TEETH": (0, 0, 0.009),
                    "TAR-JAW": (0, -0.05, -0.03),
                    "TAR-UPPER_JAW": (0, -0.05, 0),
                }

                for bone_name, (dx, dy, dz) in transformations.items():
                    bone = armature.data.edit_bones.get(bone_name)
                    if bone:
                        # Applicare la trasformazione alla tail dell'osso
                        bone.tail[0] += dx  # Sposta sull'asse X
                        bone.tail[1] += dy  # Sposta sull'asse Y
                        bone.tail[2] += dz  # Sposta sull'asse Z

                # 5. Apply roll values from roll_degree_list
                for i, bone_name in enumerate(Lista_nuovi_nomi):
                    armature = context.active_object
                    if armature and armature.type == "ARMATURE":
                        bpy.context.view_layer.objects.active = (
                            armature  # Set active object
                        )
                        bpy.ops.object.mode_set(mode="EDIT")  # Switch to Edit Mode

                        bone = armature.data.edit_bones.get(bone_name)
                        if bone:
                            bone.roll = math.radians(roll_degree_list[i])

                bpy.ops.object.mode_set(mode="OBJECT")  # Torna in modalità Object
                self.report({"INFO"}, "Armatura disposta correttamente.")
        else:
            self.report({"WARNING"}, "Per favore, seleziona un'armatura.")
        return {"FINISHED"}

class CREATE_MCH_BONES_OT_CreateMCH(bpy.types.Operator):
    bl_idname = "object.create_mch_bones"
    bl_label = "Create MCH Bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        armature = context.active_object
        if armature and armature.type == "ARMATURE":
            with bpy.context.temp_override(object=armature):
                bpy.ops.object.mode_set(mode="EDIT")  # Passa in modalità Edit

                # 1. Crea MCH-B-IK-FEET.L
                tail_pos = armature.data.edit_bones["TAR-FOOT.L"].tail.copy()
                head_pos = armature.data.edit_bones["TAR-FOOT.L"].head.copy()
                mid_pos = (tail_pos + head_pos) / 2
                new_bone_l = armature.data.edit_bones.new("MCH-B-IK-FEET.L")
                new_bone_l.head = head_pos
                new_bone_l.tail = mid_pos

                # 2. Simmetrizzazione per MCH-B-IK-FEET.R
                if "MCH-B-IK-FEET.L" in armature.data.edit_bones:
                    left_bone = armature.data.edit_bones["MCH-B-IK-FEET.L"]
                    right_bone = armature.data.edit_bones.new("MCH-B-IK-FEET.R")
                    right_bone.head = left_bone.head.copy()
                    right_bone.head.x *= -1  # Speculare lungo l'asse x
                    right_bone.tail = left_bone.tail.copy()
                    right_bone.tail.x *= -1  # Speculare lungo l'asse x
                    right_bone.roll = left_bone.roll

                # 3. Crea MCH-B-ROLL-O1-FEET.L
                roll_o1_pos = armature.data.edit_bones["TAR-FOOT.L"].tail.copy()
                roll_o1_pos.z = 0
                roll_o1_pos.y += 0.2
                new_bone_l = armature.data.edit_bones.new("MCH-B-ROLL-O1-FEET.L")
                new_bone_l.head = roll_o1_pos
                new_bone_l.tail = tail_pos
                new_bone_l.select = True  # Seleziona l'osso per l'inversione
                armature.data.edit_bones.active = new_bone_l  # Imposta come osso attivo
                # Seleziona solo MCH-B-ROLL-O1-FEET.L per l'inversione
                for bone in armature.data.edit_bones:
                    bone.select = False  # Deseleziona tutte le ossa
                armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"].select = True
                armature.data.edit_bones.active = armature.data.edit_bones[
                    "MCH-B-ROLL-O1-FEET.L"
                ]
                bpy.ops.armature.switch_direction()

                # 4. Simmetrizzazione per MCH-B-ROLL-O1-FEET.R
                if "MCH-B-ROLL-O1-FEET.L" in armature.data.edit_bones:
                    left_bone = armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"]
                    right_bone = armature.data.edit_bones.new("MCH-B-ROLL-O1-FEET.R")
                    right_bone.head = left_bone.head.copy()
                    right_bone.head.x *= -1  # Speculare lungo l'asse x
                    right_bone.tail = left_bone.tail.copy()
                    right_bone.tail.x *= -1  # Speculare lungo l'asse x
                    right_bone.roll = left_bone.roll

                # 5. Preparazione della posizione della bone CTRL-KNEE-ROLL.L
                tar_shin_head_pos = armature.data.edit_bones["TAR-SHIN.L"].head.copy()
                ctrl_knee_roll_head_pos = tar_shin_head_pos.copy()
                ctrl_knee_roll_head_pos.y += -1.0
                ctrl_knee_roll_tail_pos = tar_shin_head_pos.copy()
                ctrl_knee_roll_tail_pos.y += -1.2

                # 6. Creazione di CTRL-KNEE-ROLL.L
                new_bone_l = armature.data.edit_bones.new("CTRL-KNEE-ROLL.L")
                new_bone_l.head = ctrl_knee_roll_head_pos
                new_bone_l.tail = ctrl_knee_roll_tail_pos

                # 7. Simmetrizzazione per CTRL-KNEE-ROLL.R
                if "CTRL-KNEE-ROLL.L" in armature.data.edit_bones:
                    left_bone = armature.data.edit_bones["CTRL-KNEE-ROLL.L"]
                    right_bone = armature.data.edit_bones.new("CTRL-KNEE-ROLL.R")
                    right_bone.head = left_bone.head.copy()
                    right_bone.head.x *= -1  # Speculare lungo l'asse x
                    right_bone.tail = left_bone.tail.copy()
                    right_bone.tail.x *= -1  # Speculare lungo l'asse x
                    right_bone.roll = -90

                # Creazione della bone "PREFERENCES"
                bpy.ops.object.mode_set(mode="EDIT")

                # Ottieni la posizione della bone "TAR-HEAD"
                tar_head_bone = armature.data.edit_bones.get("TAR-HEAD")
                if tar_head_bone:
                    # Calcola la posizione per la bone "PREFERENCES"
                    preferences_head = tar_head_bone.tail.copy()
                    preferences_tail = tar_head_bone.tail.copy()
                    preferences_head.z += 0.2
                    preferences_tail.z += 0.25

                    # Crea la bone "PREFERENCES"
                    preferences_bone = armature.data.edit_bones.new("PREFERENCES")
                    preferences_bone.head = preferences_head
                    preferences_bone.tail = preferences_tail

                    print(
                        f"Bone 'PREFERENCES' created at {preferences_bone.head} with tail at {preferences_bone.tail}."
                    )

                else:
                    self.report(
                        {"ERROR"},
                        "Bone TAR-HEAD not found. 'PREFERENCES' bone creation failed.",
                    )
                    return {"CANCELLED"}

                # Copia e rinomina delle ossa
                bones_to_copy = [
                    ("TAR-LEG.L", "MCH-IK-LEG.L", "TAR-HIPS"),
                    ("TAR-LEG.R", "MCH-IK-LEG.R", "TAR-HIPS"),
                    ("TAR-SHIN.L", "MCH-IK-SHIN.L", "MCH-IK-LEG.L"),
                    ("TAR-SHIN.R", "MCH-IK-SHIN.R", "MCH-IK-LEG.R"),
                    ("TAR-FOOT.L", "MCH-IK-FOOT.L", "MCH-IK-SHIN.L"),
                    ("TAR-FOOT.R", "MCH-IK-FOOT.R", "MCH-IK-SHIN.R"),
                    ("TAR-TOE.L", "MCH-IK-TOE.L", "MCH-IK-FOOT.L"),
                    ("TAR-TOE.R", "MCH-IK-TOE.R", "MCH-IK-FOOT.R")
                ]

                for old_bone, new_bone, parent_bone in bones_to_copy:
                    if old_bone in armature.data.edit_bones:
                        copy_bone = armature.data.edit_bones.new(new_bone)
                        copy_bone.head = armature.data.edit_bones[old_bone].head.copy()
                        copy_bone.tail = armature.data.edit_bones[old_bone].tail.copy()
                        copy_bone.roll = armature.data.edit_bones[old_bone].roll
                        copy_bone.parent = armature.data.edit_bones[parent_bone]

                # Duplicazione e rinomina delle ossa FK
                bones_to_duplicate = [
                    ("TAR-LEG.L", "CTRL-FK-LEG.L", "TAR-HIPS"),
                    ("TAR-LEG.R", "CTRL-FK-LEG.R", "TAR-HIPS"),
                    ("TAR-SHIN.L", "CTRL-FK-SHIN.L", "CTRL-FK-LEG.L"),
                    ("TAR-SHIN.R", "CTRL-FK-SHIN.R", "CTRL-FK-LEG.R"),
                    ("TAR-FOOT.L", "CTRL-FK-FOOT.L", "CTRL-FK-SHIN.L"),
                    ("TAR-FOOT.R", "CTRL-FK-FOOT.R", "CTRL-FK-SHIN.R"),
                    ("TAR-TOE.L", "CTRL-FK-TOE.L", "CTRL-FK-FOOT.L"),
                    ("TAR-TOE.R", "CTRL-FK-TOE.R", "CTRL-FK-FOOT.R")
                ]

                for old_bone, new_bone, parent_bone in bones_to_duplicate:
                    if old_bone in armature.data.edit_bones:
                        duplicate_bone = armature.data.edit_bones.new(new_bone)
                        duplicate_bone.head = armature.data.edit_bones[old_bone].head.copy()
                        duplicate_bone.tail = armature.data.edit_bones[old_bone].tail.copy()
                        duplicate_bone.roll = armature.data.edit_bones[old_bone].roll
                        duplicate_bone.parent = armature.data.edit_bones[parent_bone]


                
                bpy.ops.object.mode_set(mode="OBJECT")  # Torna in modalità Object
                self.report({"INFO"}, "Bones MCH creati correttamente.")

        else:
            self.report({"WARNING"}, "Per favore, seleziona un'armatura.")
        return {"FINISHED"}


class MAKE_CTRL_BONES_OT_CreateCtrlBones(bpy.types.Operator):
    bl_idname = "object.make_ctrl_bones"
    bl_label = "Unified Operator"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # Esegui MAKE_CTRL_BONES_OT_CreateCtrlBones
        armature = context.active_object
        if armature and armature.type == "ARMATURE":
            with bpy.context.temp_override(object=armature):
                bpy.ops.object.mode_set(mode="EDIT")
                mch_roll_o2_bone_left = armature.data.edit_bones.new("MCH-B-ROLL-O2-FEET.L")
                mch_roll_o1_tail_left = armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"].tail.copy()
                mch_roll_o2_bone_left.head = mch_roll_o1_tail_left
                mch_roll_o2_bone_left.tail = mch_roll_o1_tail_left.copy()
                mch_roll_o2_bone_left.tail.z += 0.2
                if "MCH-B-ROLL-O2-FEET.L" in armature.data.edit_bones:
                    left_bone = armature.data.edit_bones["MCH-B-ROLL-O2-FEET.L"]
                    right_bone = armature.data.edit_bones.new("MCH-B-ROLL-O2-FEET.R")
                    right_bone.head = left_bone.head.copy()
                    right_bone.head.x *= -1
                    right_bone.tail = left_bone.tail.copy()
                    right_bone.tail.x *= -1
                    right_bone.roll = left_bone.roll
                ctrl_roll_foot_bone_left = armature.data.edit_bones.new("CTRL-ROLL-FOOT.L")
                ctrl_roll_foot_bone_left.head = mch_roll_o2_bone_left.head.copy()
                ctrl_roll_foot_bone_left.tail = mch_roll_o2_bone_left.tail.copy()
                ctrl_roll_foot_bone_left.head.y += 0.2
                ctrl_roll_foot_bone_left.tail.y += 0.2
                ctrl_roll_foot_bone_left.parent = mch_roll_o2_bone_left
                mch_roll_o1_head_left = armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"].head.copy()
                mch_roll_o1_tail_left = armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"].tail.copy()
                ctrl_b_foot_bone_left = armature.data.edit_bones.new("CTRL-B-FOOT.L")
                ctrl_b_foot_bone_left.tail = mch_roll_o1_tail_left
                ctrl_b_foot_bone_left.head.x = mch_roll_o1_head_left.x
                ctrl_b_foot_bone_left.head.y = mch_roll_o1_head_left.y
                ctrl_b_foot_bone_left.head.z = mch_roll_o1_tail_left.z
                if "CTRL-B-FOOT.L" in armature.data.edit_bones:
                    left_bone = armature.data.edit_bones["CTRL-B-FOOT.L"]
                    right_bone = armature.data.edit_bones.new("CTRL-B-FOOT.R")
                    right_bone.head = left_bone.head.copy()
                    right_bone.head.x *= -1
                    right_bone.tail = left_bone.tail.copy()
                    right_bone.tail.x *= -1
                    right_bone.roll = left_bone.roll
                if "CTRL-ROLL-FOOT.L" in armature.data.edit_bones:
                    left_bone = armature.data.edit_bones["CTRL-ROLL-FOOT.L"]
                    right_bone = armature.data.edit_bones.new("CTRL-ROLL-FOOT.R")
                    right_bone.head = left_bone.head.copy()
                    right_bone.head.x *= -1
                    right_bone.tail = left_bone.tail.copy()
                    right_bone.tail.x *= -1
                    right_bone.roll = left_bone.roll
                armature.data.edit_bones["MCH-IK-FOOT.L"].parent = armature.data.edit_bones["MCH-B-IK-FEET.L"]
                armature.data.edit_bones["MCH-B-IK-FEET.L"].parent = armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"]
                armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"].parent = mch_roll_o2_bone_left
                mch_roll_o2_bone_left.parent = ctrl_b_foot_bone_left
                ctrl_roll_foot_bone_left.parent = ctrl_b_foot_bone_left
                armature.data.edit_bones["MCH-B-ROLL-O1-FEET.L"].parent = armature.data.edit_bones["MCH-B-ROLL-O2-FEET.L"]
                armature.data.edit_bones["MCH-B-ROLL-O2-FEET.L"].parent = armature.data.edit_bones["CTRL-B-FOOT.L"]
                armature.data.edit_bones["CTRL-B-FOOT.L"].parent = armature.data.edit_bones["root"]
                armature.data.edit_bones["CTRL-ROLL-FOOT.L"].parent = armature.data.edit_bones["CTRL-B-FOOT.L"]
                armature.data.edit_bones["MCH-IK-FOOT.R"].parent = armature.data.edit_bones["MCH-B-IK-FEET.R"]
                armature.data.edit_bones["MCH-B-IK-FEET.R"].parent = armature.data.edit_bones["MCH-B-ROLL-O1-FEET.R"]
                armature.data.edit_bones["MCH-B-ROLL-O1-FEET.R"].parent = armature.data.edit_bones["MCH-B-ROLL-O2-FEET.R"]
                armature.data.edit_bones["MCH-B-ROLL-O2-FEET.R"].parent = armature.data.edit_bones["CTRL-B-FOOT.R"]
                armature.data.edit_bones["CTRL-B-FOOT.R"].parent = armature.data.edit_bones["root"]
                armature.data.edit_bones["CTRL-ROLL-FOOT.R"].parent = armature.data.edit_bones["CTRL-B-FOOT.R"]
                bpy.ops.object.mode_set(mode="OBJECT")
                self.report({"INFO"}, "Bones CTRL creati correttamente.")
        else:
            self.report({"WARNING"}, "Per favore, seleziona un'armatura.")
            return {"CANCELLED"}

        # Esegui ApplyConstraint_OT_ApplyConstraint
        armature = context.object
        target_bone = armature.pose.bones.get("MCH-IK-SHIN.L")
        if not target_bone:
            self.report({"ERROR"}, "Target bone MCH-IK-SHIN.L not found")
            return {"CANCELLED"}
        subtarget_bone = armature.pose.bones.get("MCH-B-IK-FEET.L")
        if not subtarget_bone:
            self.report({"ERROR"}, "Sub-target bone MCH-B-IK-FEET.L not found")
            return {"CANCELLED"}
        ik_constraint = target_bone.constraints.new(type="IK")
        ik_constraint.target = armature
        ik_constraint.subtarget = "MCH-B-IK-FEET.L"
        ik_constraint.chain_count = 2
        pole_target_bone = armature.pose.bones.get("CTRL-KNEE-ROLL.L")
        if pole_target_bone:
            ik_constraint.pole_target = armature
            ik_constraint.pole_subtarget = "CTRL-KNEE-ROLL.L"
            ik_constraint.pole_angle = 90.0
            ik_constraint.pole_angle = ik_constraint.pole_angle / 2
        roll_o1_bone = context.object.pose.bones.get("MCH-B-ROLL-O1-FEET.L")
        if not roll_o1_bone:
            self.report({"ERROR"}, "Bone MCH-B-ROLL-O1-FEET.L not found")
            return {"CANCELLED"}
        copy_rotation_constraint = roll_o1_bone.constraints.new(type="COPY_ROTATION")
        copy_rotation_constraint.target = context.object
        copy_rotation_constraint.subtarget = "CTRL-ROLL-FOOT.L"
        copy_rotation_constraint.target_space = "LOCAL"
        copy_rotation_constraint.owner_space = "LOCAL"
        limit_rotation_constraint = roll_o1_bone.constraints.new(type="LIMIT_ROTATION")
        limit_rotation_constraint.use_limit_x = True
        limit_rotation_constraint.min_x = 0
        limit_rotation_constraint.max_x = 180
        limit_rotation_constraint.owner_space = "LOCAL"
        roll_o2_bone = context.object.pose.bones.get("MCH-B-ROLL-O2-FEET.L")
        if not roll_o2_bone:
            self.report({"ERROR"}, "Bone MCH-B-ROLL-O2-FEET.L not found")
            return {"CANCELLED"}
        copy_rotation_constraint = roll_o2_bone.constraints.new(type="COPY_ROTATION")
        copy_rotation_constraint.target = context.object
        copy_rotation_constraint.subtarget = "CTRL-ROLL-FOOT.L"
        copy_rotation_constraint.target_space = "LOCAL"
        copy_rotation_constraint.owner_space = "LOCAL"
        limit_rotation_constraint = roll_o2_bone.constraints.new(type="LIMIT_ROTATION")
        limit_rotation_constraint.use_limit_x = True
        limit_rotation_constraint.min_x = -180
        limit_rotation_constraint.max_x = 0
        limit_rotation_constraint.owner_space = "LOCAL"
        toe_bone_left = context.object.pose.bones.get("MCH-IK-TOE.L")
        if not toe_bone_left:
            self.report({"ERROR"}, "Bone MCH-IK-TOE.L not found")
            return {"CANCELLED"}
        copy_rotation_constraint_toe_left = toe_bone_left.constraints.new(type="COPY_ROTATION")
        copy_rotation_constraint_toe_left.target = context.object
        copy_rotation_constraint_toe_left.subtarget = "MCH-B-ROLL-O1-FEET.L"
        copy_rotation_constraint_toe_left.target_space = "LOCAL"
        copy_rotation_constraint_toe_left.owner_space = "LOCAL"
        target_bone = armature.pose.bones.get("MCH-IK-SHIN.R")
        if not target_bone:
            self.report({"ERROR"}, "Target bone MCH-IK-SHIN.R not found")
            return {"CANCELLED"}
        subtarget_bone = armature.pose.bones.get("MCH-B-IK-FEET.R")
        if not subtarget_bone:
            self.report({"ERROR"}, "Sub-target bone MCH-B-IK-FEET.R not found")
            return {"CANCELLED"}
        ik_constraint = target_bone.constraints.new(type="IK")
        ik_constraint.target = armature
        ik_constraint.subtarget = "MCH-B-IK-FEET.R"
        ik_constraint.chain_count = 2
        pole_target_bone = armature.pose.bones.get("CTRL-KNEE-ROLL.R")
        if pole_target_bone:
            ik_constraint.pole_target = armature
            ik_constraint.pole_subtarget = "CTRL-KNEE-ROLL.R"
            ik_constraint.pole_angle = 90.0
            ik_constraint.pole_angle = ik_constraint.pole_angle / 2
        roll_o1_bone = context.object.pose.bones.get("MCH-B-ROLL-O1-FEET.R")
        if not roll_o1_bone:
            self.report({"ERROR"}, "Bone MCH-B-ROLL-O1-FEET.R not found")
            return {"CANCELLED"}
        copy_rotation_constraint = roll_o1_bone.constraints.new(type="COPY_ROTATION")
        copy_rotation_constraint.target = context.object
        copy_rotation_constraint.subtarget = "CTRL-ROLL-FOOT.R"
        copy_rotation_constraint.target_space = "LOCAL"
        copy_rotation_constraint.owner_space = "LOCAL"
        limit_rotation_constraint = roll_o1_bone.constraints.new(type="LIMIT_ROTATION")
        limit_rotation_constraint.use_limit_x = True
        limit_rotation_constraint.min_x = 0
        limit_rotation_constraint.max_x = 180
        limit_rotation_constraint.owner_space = "LOCAL"
        roll_o2_bone = context.object.pose.bones.get("MCH-B-ROLL-O2-FEET.R")
        if not roll_o2_bone:
            self.report({"ERROR"}, "Bone MCH-B-ROLL-O2-FEET.R not found")
            return {"CANCELLED"}
        copy_rotation_constraint = roll_o2_bone.constraints.new(type="COPY_ROTATION")
        copy_rotation_constraint.target = context.object
        copy_rotation_constraint.subtarget = "CTRL-ROLL-FOOT.R"
        copy_rotation_constraint.target_space = "LOCAL"
        copy_rotation_constraint.owner_space = "LOCAL"
        limit_rotation_constraint = roll_o2_bone.constraints.new(type="LIMIT_ROTATION")
        limit_rotation_constraint.use_limit_x = True
        limit_rotation_constraint.min_x = -180
        limit_rotation_constraint.max_x = 0
        limit_rotation_constraint.owner_space = "LOCAL"
        toe_bone_right = context.object.pose.bones.get("MCH-IK-TOE.R")
        if not toe_bone_right:
            self.report({"ERROR"}, "Bone MCH-IK-TOE.R not found")
            return {"CANCELLED"}
        copy_rotation_constraint_toe_right = toe_bone_right.constraints.new(type="COPY_ROTATION")
        copy_rotation_constraint_toe_right.target = context.object
        copy_rotation_constraint_toe_right.subtarget = "MCH-B-ROLL-O1-FEET.R"
        copy_rotation_constraint_toe_right.target_space = "LOCAL"
        copy_rotation_constraint_toe_right.owner_space = "LOCAL"
        bones_to_update = [
            ("MCH-IK-LEG.L", 0.05, False, False),
            ("MCH-IK-LEG.R", 0.05, False, False),
            ("MCH-IK-SHIN.L", 0.05, True, True),
            ("MCH-IK-SHIN.R", 0.05, True, True),
        ]
        for bone_name, ik_stretch, lock_ik_y, lock_ik_z in bones_to_update:
            bone = armature.pose.bones.get(bone_name)
            if bone:
                bone.ik_stretch = ik_stretch
                bone.lock_ik_y = lock_ik_y
                bone.lock_ik_z = lock_ik_z
        constraints = [
            ("TAR-LEG.L", "MCH-IK-LEG.L"),
            ("TAR-LEG.R", "MCH-IK-LEG.R"),
            ("TAR-SHIN.L", "MCH-IK-SHIN.L"),
            ("TAR-SHIN.R", "MCH-IK-SHIN.R"),
            ("TAR-FOOT.L", "MCH-IK-FOOT.L"),
            ("TAR-FOOT.R", "MCH-IK-FOOT.R"),
            ("TAR-TOE.L", "MCH-IK-TOE.L"),
            ("TAR-TOE.R", "MCH-IK-TOE.R"),
        ]
        for tar_bone, mch_bone in constraints:
            tar_pose_bone = armature.pose.bones.get(tar_bone)
            if tar_pose_bone:
                copy_rotation_constraint = tar_pose_bone.constraints.new(type='COPY_ROTATION')
                copy_rotation_constraint.target = armature
                copy_rotation_constraint.subtarget = mch_bone
                copy_location_constraint = tar_pose_bone.constraints.new(type='COPY_LOCATION')
                copy_location_constraint.target = armature
                copy_location_constraint.subtarget = mch_bone
                copy_scale_constraint = tar_pose_bone.constraints.new(type='COPY_SCALE')
                copy_scale_constraint.target = armature
                copy_scale_constraint.subtarget = mch_bone
                if 'LEG' in tar_bone or 'SHIN' in tar_bone:
                    copy_scale_constraint.use_x = False
                    copy_scale_constraint.use_z = False
        preferences_bone = armature.pose.bones.get("PREFERENCES")
        if preferences_bone:
            preferences_bone["IK/FK_Legs_Switch"] = 0.0
            ik_fk_prop = preferences_bone.id_properties_ui("IK/FK_Legs_Switch")
            ik_fk_prop.update(min=0.0, max=1.0, description="Switch between IK and FK for legs.")
        fk_constraints = [
            ("TAR-LEG.L", "CTRL-FK-LEG.L"),
            ("TAR-LEG.R", "CTRL-FK-LEG.R"),
            ("TAR-SHIN.L", "CTRL-FK-SHIN.L"),
            ("TAR-SHIN.R", "CTRL-FK-SHIN.R"),
            ("TAR-FOOT.L", "CTRL-FK-FOOT.L"),
            ("TAR-FOOT.R", "CTRL-FK-FOOT.R"),
            ("TAR-TOE.L", "CTRL-FK-TOE.L"),
            ("TAR-TOE.R", "CTRL-FK-TOE.R"),
        ]
        for tar_bone, ctrl_fk_bone in fk_constraints:
            tar_pose_bone = armature.pose.bones.get(tar_bone)
            if tar_pose_bone:
                copy_transform_constraint = tar_pose_bone.constraints.new(type='COPY_TRANSFORMS')
                copy_transform_constraint.target = armature
                copy_transform_constraint.subtarget = ctrl_fk_bone
                driver = copy_transform_constraint.driver_add("influence").driver
                driver.type = 'AVERAGE'
                var = driver.variables.new()
                var.name = 'switch'
                var.type = 'SINGLE_PROP'
                target = var.targets[0]
                target.id = armature
                target.data_path = preferences_bone.path_from_id() + '["IK/FK_Legs_Switch"]'
#####EYE RIGGING    
        if armature and armature.type == "ARMATURE":
            bpy.ops.object.mode_set(mode="EDIT")
            eye_bones = ["TAR-EYE.L", "TAR-EYE.R"]
            for eye_bone_name in eye_bones:
                try:
                    tar_bone = armature.data.edit_bones.get(eye_bone_name)
                    mch_bone_name = eye_bone_name.replace("TAR", "MCH")
                    mch_bone = armature.data.edit_bones.new(mch_bone_name)
                    mch_bone.head = tar_bone.head.copy()
                    mch_bone.tail = tar_bone.tail.copy()
                    mch_bone.roll = tar_bone.roll
                    original_length = (tar_bone.tail - tar_bone.head).length
                    new_length = original_length * 0.5
                    direction = (mch_bone.tail - mch_bone.head).normalized()
                    mch_bone.tail = mch_bone.head + direction * new_length
                    tar_bone.parent = mch_bone
                except Exception as e:
                    print(f"Error processing {eye_bone_name}: {e}")

            try:
                tar_head_bone = armature.data.edit_bones.get("TAR-HEAD")
                for mch_bone_name in ["MCH-EYE.L", "MCH-EYE.R"]:
                    mch_bone = armature.data.edit_bones.get(mch_bone_name)
                    mch_bone.parent = tar_head_bone
            except Exception as e:
                print(f"Error setting parent for head: {e}")

            for mch_bone_name in ["MCH-EYE.L", "MCH-EYE.R"]:
                try:
                    mch_bone = armature.data.edit_bones.get(mch_bone_name)
                    mch_target_bone_name = mch_bone_name.replace("MCH", "MCH-TARGET")
                    mch_target_bone = armature.data.edit_bones.new(mch_target_bone_name)
                    mch_target_bone.head = mch_bone.head.copy()
                    mch_target_bone.tail = mch_bone.tail.copy()
                    mch_target_bone.roll = mch_bone.roll
                    mch_target_bone.head.y -= 0.3
                    mch_target_bone.tail.y -= 0.3
                except Exception as e:
                    print(f"Error creating target bone {mch_bone_name}: {e}")

            bpy.ops.object.mode_set(mode="POSE")
            for mch_bone_name in ["MCH-EYE.L", "MCH-EYE.R"]:
                try:
                    mch_bone = armature.pose.bones.get(mch_bone_name)
                    mch_target_bone_name = mch_bone_name.replace("MCH", "MCH-TARGET")
                    damped_track_constraint = mch_bone.constraints.new(type="DAMPED_TRACK")
                    damped_track_constraint.target = armature
                    damped_track_constraint.subtarget = mch_target_bone_name
                except Exception as e:
                    print(f"Error adding constraint to {mch_bone_name}: {e}")

            try:
                bpy.ops.object.mode_set(mode="EDIT")
                mch_target_eye_l = armature.data.edit_bones.get("MCH-TARGET-EYE.L")
                mch_target_eye_r = armature.data.edit_bones.get("MCH-TARGET-EYE.R")
                if mch_target_eye_l and mch_target_eye_r:
                    ctrl_target_eyes = armature.data.edit_bones.new("CTRL-TARGET-EYES")
                    ctrl_target_eyes.head = (mch_target_eye_l.head + mch_target_eye_r.head) / 2
                    ctrl_target_eyes.tail = ctrl_target_eyes.head.copy()
                    ctrl_target_eyes.tail.y += 0.2
                    mch_target_eye_l.parent = ctrl_target_eyes
                    mch_target_eye_r.parent = ctrl_target_eyes
            except Exception as e:
                print(f"Error creating control target eyes: {e}")

            try:
                if ctrl_target_eyes:
                    mch_int_target_eyes = armature.data.edit_bones.new("MCH-INT-TARGET-EYES")
                    mch_int_target_eyes.head = ctrl_target_eyes.head.copy()
                    mch_int_target_eyes.tail = ctrl_target_eyes.tail.copy()
                    mch_int_target_eyes.tail = mch_int_target_eyes.head + 0.3 * (ctrl_target_eyes.tail - ctrl_target_eyes.head)
                    mch_target_eyes = armature.data.edit_bones.new("MCH-TARGET-EYES")
                    mch_target_eyes.head = mch_int_target_eyes.head.copy()
                    mch_target_eyes.tail = mch_int_target_eyes.tail.copy()
                    mch_target_eyes.tail = mch_target_eyes.head + 0.3 * (mch_int_target_eyes.tail - mch_int_target_eyes.head)
                    bpy.ops.object.mode_set(mode="EDIT")
                    mch_target_eyes = armature.data.edit_bones.get("MCH-TARGET-EYES")
                    tar_head_bone = armature.data.edit_bones.get("TAR-HEAD")
                    if mch_target_eyes and tar_head_bone:
                        mch_target_eyes.parent = tar_head_bone
                    ctrl_target_eyes.parent = mch_int_target_eyes
            except Exception as e:
                print(f"Error setting up intermediate target eyes: {e}")

            try:
                bpy.ops.object.mode_set(mode="POSE")
                mch_int_target_eyes_pose = armature.pose.bones.get("MCH-INT-TARGET-EYES")
                if mch_int_target_eyes_pose:
                    copy_transforms_constraint = mch_int_target_eyes_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_transforms_constraint.target = armature
                    copy_transforms_constraint.subtarget = "MCH-TARGET-EYES"
            except Exception as e:
                print(f"Error adding copy transforms constraint: {e}")

            try:
                bpy.ops.object.mode_set(mode="POSE")
                preferences_bone = armature.pose.bones.get("PREFERENCES")
                if preferences_bone:
                    preferences_bone["Eye-follow-head"] = 1.0
                    follow_head_prop = preferences_bone.id_properties_ui("Eye-follow-head")
                    follow_head_prop.update(min=0.0, max=1.0, description="Control whether the eyes follow the head or not.")
            except Exception as e:
                print(f"Error adding custom property: {e}")

            try:
                mch_int_target_eyes = armature.pose.bones.get("MCH-INT-TARGET-EYES")
                if mch_int_target_eyes:
                    for constraint in mch_int_target_eyes.constraints:
                        if constraint.type == "COPY_TRANSFORMS":
                            fcurve = constraint.driver_add("influence")
                            driver = fcurve.driver
                            driver.type = "AVERAGE"
                            var = driver.variables.new()
                            var.name = "EyeFollowHead"
                            var.type = "SINGLE_PROP"
                            target = var.targets[0]
                            target.id = armature
                            target.data_path = 'pose.bones["PREFERENCES"]["Eye-follow-head"]'
                            constraint.influence = 0.0
            except Exception as e:
                print(f"Error setting up driver: {e}")

            bpy.ops.object.mode_set(mode="OBJECT")
            self.report({"INFO"}, "Custom properties and driver setup completed successfully.")
        else:
            self.report({"WARNING"}, "Please select an armature.")
            return {"CANCELLED"}





        # Esegui IkFkArmsRigOperator
        armature = context.object
        if armature and armature.type == "ARMATURE":
            bpy.ops.object.mode_set(mode="EDIT")
            arm_bones = ["TAR-ARM.L", "TAR-FOREARM.L", "TAR-HAND.L"]
            new_bones = {}
            for bone_name in arm_bones:
                tar_bone = armature.data.edit_bones.get(bone_name)
                if tar_bone:
                    mch_bone_name = bone_name.replace("TAR", "MCH-IK")
                    mch_bone = armature.data.edit_bones.new(mch_bone_name)
                    mch_bone.head = tar_bone.head[:]
                    mch_bone.tail = tar_bone.tail[:]
                    mch_bone.roll = tar_bone.roll
                    mch_bone.use_connect = tar_bone.use_connect
                    new_bones[mch_bone_name] = mch_bone
            tar_forearm = armature.data.edit_bones.get("TAR-FOREARM.L")
            if tar_forearm:
                ctrl_ik_arm_l = armature.data.edit_bones.new("CTRL-IK-ARM.L")
                ctrl_ik_arm_l.head = tar_forearm.tail[:]
                ctrl_ik_arm_l.tail = (ctrl_ik_arm_l.head[0], ctrl_ik_arm_l.head[1] + 0.09, ctrl_ik_arm_l.head[2])
                ctrl_ik_arm_l.roll = tar_forearm.roll
                ctrl_ik_arm_l.parent = armature.data.edit_bones.get("root")
            mch_ik_hand_l = armature.data.edit_bones.get("MCH-IK-HAND.L")
            if mch_ik_hand_l and ctrl_ik_arm_l:
                mch_ik_hand_l.parent = ctrl_ik_arm_l
            tar_arm = armature.data.edit_bones.get("TAR-ARM.L")
            if tar_arm:
                ctrl_roll_elbow_l = armature.data.edit_bones.new("CTRL-ROLL-ELBOW.L")
                ctrl_roll_elbow_l.head = tar_arm.tail[:]
                ctrl_roll_elbow_l.tail = (ctrl_roll_elbow_l.head[0], ctrl_roll_elbow_l.head[1] + 0.03, ctrl_roll_elbow_l.head[2])
                ctrl_roll_elbow_l.roll = tar_arm.roll
                ctrl_roll_elbow_l.parent = armature.data.edit_bones.get("CTRL-IK-ARM.L")
                ctrl_roll_elbow_l.head[1] += 0.1
                ctrl_roll_elbow_l.tail[1] += 0.1
            mch_ik_forearm_l = new_bones.get("MCH-IK-FOREARM.L")
            mch_ik_arm_l = new_bones.get("MCH-IK-ARM.L")
            tar_shoulder_l = armature.data.edit_bones.get("TAR-SHOULDER.L")
            if mch_ik_forearm_l and mch_ik_arm_l:
                mch_ik_forearm_l.parent = mch_ik_arm_l
            if mch_ik_arm_l and tar_shoulder_l:
                mch_ik_arm_l.parent = tar_shoulder_l
            bpy.ops.object.mode_set(mode="POSE")
            mch_ik_forearm_pose = armature.pose.bones.get("MCH-IK-FOREARM.L")
            if mch_ik_forearm_pose:
                ik_constraint = mch_ik_forearm_pose.constraints.new(type="IK")
                ik_constraint.target = armature
                ik_constraint.subtarget = "CTRL-IK-ARM.L"
                ik_constraint.pole_target = armature
                ik_constraint.pole_subtarget = "CTRL-ROLL-ELBOW.L"
                ik_constraint.pole_angle = 180
                ik_constraint.chain_count = 2
            mch_ik_forearm_pose.ik_stretch = 0.05
            mch_ik_forearm_pose.lock_ik_x = True
            mch_ik_forearm_pose.lock_ik_y = True
            mch_ik_arm_pose = armature.pose.bones.get("MCH-IK-ARM.L")
            if mch_ik_arm_pose:
                mch_ik_arm_pose.ik_stretch = 0.05
            bpy.ops.object.mode_set(mode="EDIT")
            arm_bones = ["TAR-ARM.L", "TAR-FOREARM.L", "TAR-HAND.L"]
            for bone_name in arm_bones:
                tar_bone = armature.data.edit_bones.get(bone_name)
                if tar_bone:
                    ctrl_fk_bone_name = bone_name.replace("TAR", "CTRL-FK")
                    ctrl_fk_bone = armature.data.edit_bones.new(ctrl_fk_bone_name)
                    ctrl_fk_bone.head = tar_bone.head[:]
                    ctrl_fk_bone.tail = tar_bone.tail[:]
                    ctrl_fk_bone.roll = tar_bone.roll
                    ctrl_fk_bone.use_connect = tar_bone.use_connect
            ctrl_fk_hand_l = armature.data.edit_bones.get("CTRL-FK-HAND.L")
            ctrl_fk_forearm_l = armature.data.edit_bones.get("CTRL-FK-FOREARM.L")
            ctrl_fk_arm_l = armature.data.edit_bones.get("CTRL-FK-ARM.L")
            if ctrl_fk_hand_l and ctrl_fk_forearm_l and ctrl_fk_arm_l:
                ctrl_fk_hand_l.parent = ctrl_fk_forearm_l
                ctrl_fk_forearm_l.parent = ctrl_fk_arm_l
            mch_arm_follow_l = armature.data.edit_bones.new("MCH-ARM-FOLLOW.L")
            if ctrl_fk_arm_l:
                mch_arm_follow_l.head = ctrl_fk_arm_l.head[:]
                mch_arm_follow_l.tail = (mch_arm_follow_l.head[0], mch_arm_follow_l.head[1] + 0.09, mch_arm_follow_l.head[2])
                mch_arm_follow_l.roll = ctrl_fk_arm_l.roll
                mch_arm_follow_l.parent = armature.data.edit_bones.get("TAR-SHOULDER.L")
            mch_const_arm_follow_l = armature.data.edit_bones.new("MCH-CONST-ARM-FOLLOW.L")
            mch_const_arm_follow_l.head = mch_arm_follow_l.head[:]
            mch_const_arm_follow_l.tail = mch_arm_follow_l.tail[:]
            mch_const_arm_follow_l.roll = mch_arm_follow_l.roll
            mch_const_arm_follow_l.parent = armature.data.edit_bones.get("root")
            if ctrl_fk_arm_l and mch_const_arm_follow_l:
                ctrl_fk_arm_l.parent = mch_const_arm_follow_l
            bpy.ops.object.mode_set(mode="POSE")
            preferences_bone = armature.pose.bones.get("PREFERENCES")
            if preferences_bone:
                preferences_bone["Left_Arm_Follow"] = 1.0
                follow_arm_prop = preferences_bone.id_properties_ui("Left_Arm_Follow")
                follow_arm_prop.update(min=0.0, max=1.0, description="Controls the IK-FK blending for the left arm.")
            mch_const_arm_follow_pose = armature.pose.bones.get("MCH-CONST-ARM-FOLLOW.L")
            mch_arm_follow_pose = armature.pose.bones.get("MCH-ARM-FOLLOW.L")
            if mch_const_arm_follow_pose and mch_arm_follow_pose:
                copy_loc = mch_const_arm_follow_pose.constraints.new(type="COPY_LOCATION")
                copy_loc.target = armature
                copy_loc.subtarget = mch_arm_follow_pose.name
                copy_scale = mch_const_arm_follow_pose.constraints.new(type="COPY_SCALE")
                copy_scale.target = armature
                copy_scale.subtarget = mch_arm_follow_pose.name
                copy_rot = mch_const_arm_follow_pose.constraints.new(type="COPY_ROTATION")
                copy_rot.name = "COPY ROTATION- ARM FOLLOW"
                copy_rot.target = armature
                copy_rot.subtarget = mch_arm_follow_pose.name
                fcurve = copy_rot.driver_add("influence")
                driver = fcurve.driver
                driver.type = "AVERAGE"
                var = driver.variables.new()
                var.name = "Left_Arm_Follow"
                var.targets[0].id = armature
                var.targets[0].data_path = 'pose.bones["PREFERENCES"]["Left_Arm_Follow"]'
                if preferences_bone:
                    preferences_bone["IK/FK_Switch_Left_Arm"] = 1.0
                    ik_fk_switch_prop = preferences_bone.id_properties_ui("IK/FK_Switch_Left_Arm")
                    ik_fk_switch_prop.update(min=0.0, max=1.0, description="Controls the IK-FK switching for the left arm.")
                tar_arm_pose = armature.pose.bones.get("TAR-ARM.L")
                if tar_arm_pose:
                    copy_rot_arm = tar_arm_pose.constraints.new(type="COPY_ROTATION")
                    copy_rot_arm.target = armature
                    copy_rot_arm.subtarget = "MCH-IK-ARM.L"
                    copy_loc_arm = tar_arm_pose.constraints.new(type="COPY_LOCATION")
                    copy_loc_arm.target = armature
                    copy_loc_arm.subtarget = "MCH-IK-ARM.L"
                    copy_scale_arm = tar_arm_pose.constraints.new(type="COPY_SCALE")
                    copy_scale_arm.target = armature
                    copy_scale_arm.subtarget = "MCH-IK-ARM.L"
                    copy_scale_arm.use_x = False
                    copy_scale_arm.use_z = False
                    copy_trans_arm = tar_arm_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_trans_arm.target = armature
                    copy_trans_arm.subtarget = "CTRL-FK-ARM.L"
                    fcurve_arm = copy_trans_arm.driver_add("influence")
                    driver_arm = fcurve_arm.driver
                    driver_arm.type = "AVERAGE"
                    var_arm = driver_arm.variables.new()
                    var_arm.name = "IK/FK_Switch_Left_Arm"
                    var_arm.targets[0].id = armature
                    var_arm.targets[0].data_path = 'pose.bones["PREFERENCES"]["IK/FK_Switch_Left_Arm"]'
                tar_forearm_pose = armature.pose.bones.get("TAR-FOREARM.L")
                if tar_forearm_pose:
                    copy_rot_forearm = tar_forearm_pose.constraints.new(type="COPY_ROTATION")
                    copy_rot_forearm.target = armature
                    copy_rot_forearm.subtarget = "MCH-IK-FOREARM.L"
                    copy_loc_forearm = tar_forearm_pose.constraints.new(type="COPY_LOCATION")
                    copy_loc_forearm.target = armature
                    copy_loc_forearm.subtarget = "MCH-IK-FOREARM.L"
                    copy_scale_forearm = tar_forearm_pose.constraints.new(type="COPY_SCALE")
                    copy_scale_forearm.target = armature
                    copy_scale_forearm.subtarget = "MCH-IK-FOREARM.L"
                    copy_scale_forearm.use_x = False
                    copy_scale_forearm.use_z = False
                    copy_trans_forearm = tar_forearm_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_trans_forearm.target = armature
                    copy_trans_forearm.subtarget = "CTRL-FK-FOREARM.L"
                    fcurve_forearm = copy_trans_forearm.driver_add("influence")
                    driver_forearm = fcurve_forearm.driver
                    driver_forearm.type = "AVERAGE"
                    var_forearm = driver_forearm.variables.new()
                    var_forearm.name = "IK/FK_Switch_Left_Arm"
                    var_forearm.targets[0].id = armature
                    var_forearm.targets[0].data_path = 'pose.bones["PREFERENCES"]["IK/FK_Switch_Left_Arm"]'
                tar_hand_pose = armature.pose.bones.get("TAR-HAND.L")
                if tar_hand_pose:
                    copy_transform_hand = tar_hand_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_transform_hand.target = armature
                    copy_transform_hand.subtarget = "MCH-IK-HAND.L"
                    copy_trans_hand = tar_hand_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_trans_hand.target = armature
                    copy_trans_hand.subtarget = "CTRL-FK-HAND.L"
                    fcurve_hand = copy_trans_hand.driver_add("influence")
                    driver_hand = fcurve_hand.driver
                    driver_hand.type = "AVERAGE"
                    var_hand = driver_hand.variables.new()
                    var_hand.name = "IK/FK_Switch_Left_Arm"
                    var_hand.targets[0].id = armature
                    var_hand.targets[0].data_path = 'pose.bones["PREFERENCES"]["IK/FK_Switch_Left_Arm"]'
            bpy.ops.object.mode_set(mode="EDIT")
            arm_bones = ["TAR-ARM.R", "TAR-FOREARM.R", "TAR-HAND.R"]
            new_bones = {}
            for bone_name in arm_bones:
                tar_bone = armature.data.edit_bones.get(bone_name)
                if tar_bone:
                    mch_bone_name = bone_name.replace("TAR", "MCH-IK")
                    mch_bone = armature.data.edit_bones.new(mch_bone_name)
                    mch_bone.head = tar_bone.head[:]
                    mch_bone.tail = tar_bone.tail[:]
                    mch_bone.roll = tar_bone.roll
                    mch_bone.use_connect = tar_bone.use_connect
                    new_bones[mch_bone_name] = mch_bone
            tar_forearm = armature.data.edit_bones.get("TAR-FOREARM.R")
            if tar_forearm:
                ctrl_ik_arm_r = armature.data.edit_bones.new("CTRL-IK-ARM.R")
                ctrl_ik_arm_r.head = tar_forearm.tail[:]
                ctrl_ik_arm_r.tail = (ctrl_ik_arm_r.head[0], ctrl_ik_arm_r.head[1] + 0.09, ctrl_ik_arm_r.head[2])
                ctrl_ik_arm_r.roll = tar_forearm.roll
                ctrl_ik_arm_r.parent = armature.data.edit_bones.get("root")
            mch_ik_hand_r = armature.data.edit_bones.get("MCH-IK-HAND.R")
            if mch_ik_hand_r and ctrl_ik_arm_r:
                mch_ik_hand_r.parent = ctrl_ik_arm_r
            tar_arm = armature.data.edit_bones.get("TAR-ARM.R")
            if tar_arm:
                ctrl_roll_elbow_r = armature.data.edit_bones.new("CTRL-ROLL-ELBOW.R")
                ctrl_roll_elbow_r.head = tar_arm.tail[:]
                ctrl_roll_elbow_r.tail = (ctrl_roll_elbow_r.head[0], ctrl_roll_elbow_r.head[1] + 0.03, ctrl_roll_elbow_r.head[2])
                ctrl_roll_elbow_r.roll = tar_arm.roll
                ctrl_roll_elbow_r.parent = armature.data.edit_bones.get("CTRL-IK-ARM.R")
                ctrl_roll_elbow_r.head[1] += 0.1
                ctrl_roll_elbow_r.tail[1] += 0.1
            mch_ik_forearm_r = new_bones.get("MCH-IK-FOREARM.R")
            mch_ik_arm_r = new_bones.get("MCH-IK-ARM.R")
            tar_shoulder_r = armature.data.edit_bones.get("TAR-SHOULDER.R")
            if mch_ik_forearm_r and mch_ik_arm_r:
                mch_ik_forearm_r.parent = mch_ik_arm_r
            if mch_ik_arm_r and tar_shoulder_r:
                mch_ik_arm_r.parent = tar_shoulder_r
            bpy.ops.object.mode_set(mode="POSE")
            mch_ik_forearm_pose = armature.pose.bones.get("MCH-IK-FOREARM.R")
            if mch_ik_forearm_pose:
                ik_constraint = mch_ik_forearm_pose.constraints.new(type="IK")
                ik_constraint.target = armature
                ik_constraint.subtarget = "CTRL-IK-ARM.R"
                ik_constraint.pole_target = armature
                ik_constraint.pole_subtarget = "CTRL-ROLL-ELBOW.R"
                ik_constraint.pole_angle = 0
                ik_constraint.chain_count = 2
            mch_ik_forearm_pose.ik_stretch = 0.05
            mch_ik_forearm_pose.lock_ik_x = True
            mch_ik_forearm_pose.lock_ik_y = True
            mch_ik_arm_pose = armature.pose.bones.get("MCH-IK-ARM.R")
            if mch_ik_arm_pose:
                mch_ik_arm_pose.ik_stretch = 0.05
            bpy.ops.object.mode_set(mode="EDIT")
            arm_bones = ["TAR-ARM.R", "TAR-FOREARM.R", "TAR-HAND.R"]
            for bone_name in arm_bones:
                tar_bone = armature.data.edit_bones.get(bone_name)
                if tar_bone:
                    ctrl_fk_bone_name = bone_name.replace("TAR", "CTRL-FK")
                    ctrl_fk_bone = armature.data.edit_bones.new(ctrl_fk_bone_name)
                    ctrl_fk_bone.head = tar_bone.head[:]
                    ctrl_fk_bone.tail = tar_bone.tail[:]
                    ctrl_fk_bone.roll = tar_bone.roll
                    ctrl_fk_bone.use_connect = tar_bone.use_connect
            ctrl_fk_hand_r = armature.data.edit_bones.get("CTRL-FK-HAND.R")
            ctrl_fk_forearm_r = armature.data.edit_bones.get("CTRL-FK-FOREARM.R")
            ctrl_fk_arm_r = armature.data.edit_bones.get("CTRL-FK-ARM.R")
            if ctrl_fk_hand_r and ctrl_fk_forearm_r and ctrl_fk_arm_r:
                ctrl_fk_hand_r.parent = ctrl_fk_forearm_r
                ctrl_fk_forearm_r.parent = ctrl_fk_arm_r
            mch_arm_follow_r = armature.data.edit_bones.new("MCH-ARM-FOLLOW.R")
            if ctrl_fk_arm_r:
                mch_arm_follow_r.head = ctrl_fk_arm_r.head[:]
                mch_arm_follow_r.tail = (mch_arm_follow_r.head[0], mch_arm_follow_r.head[1] + 0.09, mch_arm_follow_r.head[2])
                mch_arm_follow_r.roll = ctrl_fk_arm_r.roll
                mch_arm_follow_r.parent = armature.data.edit_bones.get("TAR-SHOULDER.R")
            mch_const_arm_follow_r = armature.data.edit_bones.new("MCH-CONST-ARM-FOLLOW.R")
            mch_const_arm_follow_r.head = mch_arm_follow_r.head[:]
            mch_const_arm_follow_r.tail = mch_arm_follow_r.tail[:]
            mch_const_arm_follow_r.roll = mch_arm_follow_r.roll
            mch_const_arm_follow_r.parent = armature.data.edit_bones.get("root")
            if ctrl_fk_arm_r and mch_const_arm_follow_r:
                ctrl_fk_arm_r.parent = mch_const_arm_follow_r
            bpy.ops.object.mode_set(mode="POSE")
            preferences_bone = armature.pose.bones.get("PREFERENCES")
            if preferences_bone:
                preferences_bone["Right_Arm_Follow"] = 1.0
                follow_arm_prop = preferences_bone.id_properties_ui("Right_Arm_Follow")
                follow_arm_prop.update(min=0.0, max=1.0, description="Controls the IK-FK blending for the right arm.")
            mch_const_arm_follow_pose = armature.pose.bones.get("MCH-CONST-ARM-FOLLOW.R")
            mch_arm_follow_pose = armature.pose.bones.get("MCH-ARM-FOLLOW.R")
            if mch_const_arm_follow_pose and mch_arm_follow_pose:
                copy_loc = mch_const_arm_follow_pose.constraints.new(type="COPY_LOCATION")
                copy_loc.target = armature
                copy_loc.subtarget = mch_arm_follow_pose.name
                copy_scale = mch_const_arm_follow_pose.constraints.new(type="COPY_SCALE")
                copy_scale.target = armature
                copy_scale.subtarget = mch_arm_follow_pose.name
                copy_rot = mch_const_arm_follow_pose.constraints.new(type="COPY_ROTATION")
                copy_rot.name = "COPY ROTATION- ARM FOLLOW"
                copy_rot.target = armature
                copy_rot.subtarget = mch_arm_follow_pose.name
                fcurve = copy_rot.driver_add("influence")
                driver = fcurve.driver
                driver.type = "AVERAGE"
                var = driver.variables.new()
                var.name = "Right_Arm_Follow"
                var.targets[0].id = armature
                var.targets[0].data_path = 'pose.bones["PREFERENCES"]["Right_Arm_Follow"]'
                if preferences_bone:
                    preferences_bone["IK/FK_Switch_Right_Arm"] = 1.0
                    ik_fk_switch_prop = preferences_bone.id_properties_ui("IK/FK_Switch_Right_Arm")
                    ik_fk_switch_prop.update(min=0.0, max=1.0, description="Controls the IK-FK switching for the right arm.")
                tar_arm_pose = armature.pose.bones.get("TAR-ARM.R")
                if tar_arm_pose:
                    copy_rot_arm = tar_arm_pose.constraints.new(type="COPY_ROTATION")
                    copy_rot_arm.target = armature
                    copy_rot_arm.subtarget = "MCH-IK-ARM.R"
                    copy_loc_arm = tar_arm_pose.constraints.new(type="COPY_LOCATION")
                    copy_loc_arm.target = armature
                    copy_loc_arm.subtarget = "MCH-IK-ARM.R"
                    copy_scale_arm = tar_arm_pose.constraints.new(type="COPY_SCALE")
                    copy_scale_arm.target = armature
                    copy_scale_arm.subtarget = "MCH-IK-ARM.R"
                    copy_scale_arm.use_x = False
                    copy_scale_arm.use_z = False
                    copy_trans_arm = tar_arm_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_trans_arm.target = armature
                    copy_trans_arm.subtarget = "CTRL-FK-ARM.R"
                    fcurve_arm = copy_trans_arm.driver_add("influence")
                    driver_arm = fcurve_arm.driver
                    driver_arm.type = "AVERAGE"
                    var_arm = driver_arm.variables.new()
                    var_arm.name = "IK/FK_Switch_Right_Arm"
                    var_arm.targets[0].id = armature
                    var_arm.targets[0].data_path = 'pose.bones["PREFERENCES"]["IK/FK_Switch_Right_Arm"]'
                tar_forearm_pose = armature.pose.bones.get("TAR-FOREARM.R")
                if tar_forearm_pose:
                    copy_rot_forearm = tar_forearm_pose.constraints.new(type="COPY_ROTATION")
                    copy_rot_forearm.target = armature
                    copy_rot_forearm.subtarget = "MCH-IK-FOREARM.R"
                    copy_loc_forearm = tar_forearm_pose.constraints.new(type="COPY_LOCATION")
                    copy_loc_forearm.target = armature
                    copy_loc_forearm.subtarget = "MCH-IK-FOREARM.R"
                    copy_scale_forearm = tar_forearm_pose.constraints.new(type="COPY_SCALE")
                    copy_scale_forearm.target = armature
                    copy_scale_forearm.subtarget = "MCH-IK-FOREARM.R"
                    copy_scale_forearm.use_x = False
                    copy_scale_forearm.use_z = False
                    copy_trans_forearm = tar_forearm_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_trans_forearm.target = armature
                    copy_trans_forearm.subtarget = "CTRL-FK-FOREARM.R"
                    fcurve_forearm = copy_trans_forearm.driver_add("influence")
                    driver_forearm = fcurve_forearm.driver
                    driver_forearm.type = "AVERAGE"
                    var_forearm = driver_forearm.variables.new()
                    var_forearm.name = "IK/FK_Switch_Right_Arm"
                    var_forearm.targets[0].id = armature
                    var_forearm.targets[0].data_path = 'pose.bones["PREFERENCES"]["IK/FK_Switch_Right_Arm"]'
                tar_hand_pose = armature.pose.bones.get("TAR-HAND.R")
                if tar_hand_pose:
                    copy_transform_hand = tar_hand_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_transform_hand.target = armature
                    copy_transform_hand.subtarget = "MCH-IK-HAND.R"
                    copy_trans_hand = tar_hand_pose.constraints.new(type="COPY_TRANSFORMS")
                    copy_trans_hand.target = armature
                    copy_trans_hand.subtarget = "CTRL-FK-HAND.R"
                    fcurve_hand = copy_trans_hand.driver_add("influence")
                    driver_hand = fcurve_hand.driver
                    driver_hand.type = "AVERAGE"
                    var_hand = driver_hand.variables.new()
                    var_hand.name = "IK/FK_Switch_Right_Arm"
                    var_hand.targets[0].id = armature
                    var_hand.targets[0].data_path = 'pose.bones["PREFERENCES"]["IK/FK_Switch_Right_Arm"]'
            bpy.ops.object.mode_set(mode="OBJECT")
            self.report({"INFO"}, "Ik/Fk Arms Rig setup completed successfully.")
        else:
            self.report({"WARNING"}, "Please select an armature.")
            return {"CANCELLED"}

        # Esegui BodyControlOperator
        armature = context.object
        if armature and armature.type == "ARMATURE":
            bpy.ops.object.mode_set(mode="EDIT")
            tar_upper_body = armature.data.edit_bones.get("TAR-UPPER BODY")
            if tar_upper_body:
                tar_upper_body.tail[0] = tar_upper_body.head[0]
                tar_upper_body.tail[1] = tar_upper_body.head[1] + 0.2
                tar_upper_body.tail[2] = tar_upper_body.head[2]
            tar_spine = armature.data.edit_bones.get("TAR-SPINE")
            tar_spine_02 = armature.data.edit_bones.get("TAR-SPINE-02")
            if tar_spine and tar_spine_02:
                tar_spine.parent = tar_spine_02
            tar_hips = armature.data.edit_bones.get("TAR-HIPS")
            if tar_hips and tar_upper_body:
                tar_hips.parent = tar_upper_body
            ctrl_chest = armature.data.edit_bones.new("CTRL-CHEST")
            tar_chest = armature.data.edit_bones.get("TAR-CHEST")
            if tar_chest and tar_upper_body:
                ctrl_chest.head = tar_upper_body.head[:]
                ctrl_chest.tail = tar_chest.tail[:]
                ctrl_chest.roll = tar_chest.roll
            bpy.ops.object.mode_set(mode="POSE")
            bones_with_constraints = ["TAR-CHEST", "TAR-SPINE", "TAR-SPINE-02"]
            for bone_name in bones_with_constraints:
                bone = armature.pose.bones.get(bone_name)
                if bone:
                    copy_transform = bone.constraints.new(type="COPY_TRANSFORMS")
                    copy_transform.target = armature
                    copy_transform.subtarget = "CTRL-CHEST"
                    copy_transform.mix_mode = 'BEFORE_FULL'
                    copy_transform.target_space = 'LOCAL'
                    copy_transform.owner_space = 'LOCAL'
            bpy.ops.object.mode_set(mode="OBJECT")
            self.report({"INFO"}, "Body control setup completed successfully.")
        else:
            self.report({"WARNING"}, "Please select an armature.")
            return {"CANCELLED"}

        # Esegui FingersConstraintOperator
        armature = context.object
        if armature and armature.type == "ARMATURE":
            bpy.ops.object.mode_set(mode="EDIT")
            finger_bones = [
                ("TAR-FINGER-A-01.R", "CTRL-FINGER-A-01.R"),
                ("TAR-FINGER-B-01.R", "CTRL-FINGER-B-01.R"),
                ("TAR-FINGER-C-01.R", "CTRL-FINGER-C-01.R"),
                ("TAR-FINGER-D-01.R", "CTRL-FINGER-D-01.R"),
                ("TAR-FINGER-E-01.R", "CTRL-FINGER-E-01.R"),
                ("TAR-FINGER-A-01.L", "CTRL-FINGER-A-01.L"),
                ("TAR-FINGER-B-01.L", "CTRL-FINGER-B-01.L"),
                ("TAR-FINGER-C-01.L", "CTRL-FINGER-C-01.L"),
                ("TAR-FINGER-D-01.L", "CTRL-FINGER-D-01.L"),
                ("TAR-FINGER-E-01.L", "CTRL-FINGER-E-01.L")
            ]
            for orig_bone_name, new_bone_name in finger_bones:
                try:
                    tar_bone = armature.data.edit_bones[orig_bone_name]
                    new_bone = armature.data.edit_bones.new(new_bone_name)
                    new_bone.head = tar_bone.head[:]
                    new_bone.tail = tar_bone.tail[:]
                    new_bone.roll = tar_bone.roll
                    new_bone.use_connect = tar_bone.use_connect
                    new_bone.parent = armature.data.edit_bones.get("TAR-HAND")
                    tail_vector = new_bone.tail - new_bone.head
                    tail_vector.normalize()
                    new_bone.tail += tail_vector * 0.03
                except KeyError:
                    self.report({"WARNING"}, f"{orig_bone_name} not found. Skipping.")
                    continue
            bones_to_extract = [
                "CTRL-FINGER-A-01.R", "CTRL-FINGER-B-01.R", "CTRL-FINGER-C-01.R", 
                "CTRL-FINGER-D-01.R", "CTRL-FINGER-E-01.R", "CTRL-FINGER-A-01.L", 
                "CTRL-FINGER-B-01.L", "CTRL-FINGER-C-01.L", "CTRL-FINGER-D-01.L", 
                "CTRL-FINGER-E-01.L"
            ]
            for bone_name in bones_to_extract:
                bone = armature.data.edit_bones.get(bone_name)
                if bone:
                    bpy.ops.armature.select_all(action='DESELECT')
                    bone.select = True
                    armature.data.edit_bones.active = bone
                    bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value":(0, 0, 0)})
                    new_bone = armature.data.edit_bones.active
                    new_bone_name = bone_name.replace("01", "02")
                    new_bone.name = new_bone_name
                    new_bone.head = bone.tail[:]
                    new_bone.tail = (bone.tail[0], bone.tail[1] + 0.03, bone.tail[2])
                    new_bone.parent = bone
            bpy.ops.object.mode_set(mode='EDIT')
            bones_01 = [
                "CTRL-FINGER-A-01.R", "CTRL-FINGER-B-01.R", "CTRL-FINGER-C-01.R", 
                "CTRL-FINGER-D-01.R", "CTRL-FINGER-E-01.R", "CTRL-FINGER-A-01.L", 
                "CTRL-FINGER-B-01.L", "CTRL-FINGER-C-01.L", "CTRL-FINGER-D-01.L", 
                "CTRL-FINGER-E-01.L"
            ]
            for bone_01 in bones_01:
                bone_02 = bone_01.replace("01", "02")
                bone_01_edit = armature.data.edit_bones.get(bone_01)
                bone_02_edit = armature.data.edit_bones.get(bone_02)
                if bone_01_edit and bone_02_edit:
                    armature.data.edit_bones.active = bone_01_edit
                    bpy.ops.armature.select_all(action='DESELECT')
                    bone_02_edit.select = True
                    bone_01_edit.select = True
                    armature.data.edit_bones.active = bone_01_edit
                    bpy.ops.armature.align()
            bpy.ops.object.mode_set(mode='POSE')
            finger_bones_r = ["TAR-FINGER-A-01.R", "TAR-FINGER-B-01.R", "TAR-FINGER-C-01.R", "TAR-FINGER-D-01.R", "TAR-FINGER-E-01.R"]
            ctrl_finger_bones_r = ["CTRL-FINGER-A-01.R", "CTRL-FINGER-B-01.R", "CTRL-FINGER-C-01.R", "CTRL-FINGER-D-01.R", "CTRL-FINGER-E-01.R"]
            for tar_bone, ctrl_bone in zip(finger_bones_r, ctrl_finger_bones_r):
                bone = armature.pose.bones.get(tar_bone)
                if bone:
                    copy_transform = bone.constraints.new(type='COPY_TRANSFORMS')
                    copy_transform.target = armature
                    copy_transform.subtarget = ctrl_bone
                    copy_transform.mix_mode = 'REPLACE'
                    copy_transform.target_space = 'LOCAL'
                    copy_transform.owner_space = 'LOCAL'
            finger_end_bones_r = ["TAR-FINGER-E-03.R", "TAR-FINGER-D-03.R", "TAR-FINGER-C-03.R", "TAR-FINGER-B-03.R", "TAR-FINGER-A-03.R"]
            ctrl_finger_end_bones_r = ["CTRL-FINGER-E-02.R", "CTRL-FINGER-D-02.R", "CTRL-FINGER-C-02.R", "CTRL-FINGER-B-02.R", "CTRL-FINGER-A-02.R"]
            for tar_bone, ctrl_bone in zip(finger_end_bones_r, ctrl_finger_end_bones_r):
                bone = armature.pose.bones.get(tar_bone)
                if bone:
                    copy_rotation = bone.constraints.new(type='COPY_ROTATION')
                    copy_rotation.target = armature
                    copy_rotation.subtarget = ctrl_bone
                    copy_rotation.mix_mode = 'REPLACE'
                    copy_rotation.target_space = 'LOCAL'
                    copy_rotation.owner_space = 'LOCAL'
            finger_mid_bones_r = ["TAR-FINGER-E-02.R", "TAR-FINGER-D-02.R", "TAR-FINGER-C-02.R", "TAR-FINGER-B-02.R", "TAR-FINGER-A-02.R"]
            ctrl_finger_mid_bones_r = ["CTRL-FINGER-E-02.R", "CTRL-FINGER-D-02.R", "CTRL-FINGER-C-02.R", "CTRL-FINGER-B-02.R", "CTRL-FINGER-A-02.R"]
            for tar_bone, ctrl_bone in zip(finger_mid_bones_r, ctrl_finger_mid_bones_r):
                bone = armature.pose.bones.get(tar_bone)
                if bone:
                    copy_rotation = bone.constraints.new(type='COPY_ROTATION')
                    copy_rotation.target = armature
                    copy_rotation.subtarget = ctrl_bone
                    copy_rotation.mix_mode = 'REPLACE'
                    copy_rotation.target_space = 'LOCAL'
                    copy_rotation.owner_space = 'LOCAL'
            finger_bones_l = ["TAR-FINGER-A-01.L", "TAR-FINGER-B-01.L", "TAR-FINGER-C-01.L", "TAR-FINGER-D-01.L", "TAR-FINGER-E-01.L"]
            ctrl_finger_bones_l = ["CTRL-FINGER-A-01.L", "CTRL-FINGER-B-01.L", "CTRL-FINGER-C-01.L", "CTRL-FINGER-D-01.L", "CTRL-FINGER-E-01.L"]
            for tar_bone, ctrl_bone in zip(finger_bones_l, ctrl_finger_bones_l):
                bone = armature.pose.bones.get(tar_bone)
                if bone:
                    copy_transform = bone.constraints.new(type='COPY_TRANSFORMS')
                    copy_transform.target = armature
                    copy_transform.subtarget = ctrl_bone
                    copy_transform.mix_mode = 'REPLACE'
                    copy_transform.target_space = 'LOCAL'
                    copy_transform.owner_space = 'LOCAL'
            finger_end_bones_l = ["TAR-FINGER-E-03.L", "TAR-FINGER-D-03.L", "TAR-FINGER-C-03.L", "TAR-FINGER-B-03.L", "TAR-FINGER-A-03.L"]
            ctrl_finger_end_bones_l = ["CTRL-FINGER-E-02.L", "CTRL-FINGER-D-02.L", "CTRL-FINGER-C-02.L", "CTRL-FINGER-B-02.L", "CTRL-FINGER-A-02.L"]
            for tar_bone, ctrl_bone in zip(finger_end_bones_l, ctrl_finger_end_bones_l):
                bone = armature.pose.bones.get(tar_bone)
                if bone:
                    copy_rotation = bone.constraints.new(type='COPY_ROTATION')
                    copy_rotation.target = armature
                    copy_rotation.subtarget = ctrl_bone
                    copy_rotation.mix_mode = 'REPLACE'
                    copy_rotation.target_space = 'LOCAL'
                    copy_rotation.owner_space = 'LOCAL'
            finger_mid_bones_l = ["TAR-FINGER-E-02.L", "TAR-FINGER-D-02.L", "TAR-FINGER-C-02.L", "TAR-FINGER-B-02.L", "TAR-FINGER-A-02.L"]
            ctrl_finger_mid_bones_l = ["CTRL-FINGER-E-02.L", "CTRL-FINGER-D-02.L", "CTRL-FINGER-C-02.L", "CTRL-FINGER-B-02.L", "CTRL-FINGER-A-02.L"]
            for tar_bone, ctrl_bone in zip(finger_mid_bones_l, ctrl_finger_mid_bones_l):
                bone = armature.pose.bones.get(tar_bone)
                if bone:
                    copy_rotation = bone.constraints.new(type='COPY_ROTATION')
                    copy_rotation.target = armature
                    copy_rotation.subtarget = ctrl_bone
                    copy_rotation.mix_mode = 'REPLACE'
                    copy_rotation.target_space = 'LOCAL'
                    copy_rotation.owner_space = 'LOCAL'







            bpy.ops.object.mode_set(mode="EDIT")

            # Parentare le ossa sinistre a TAR-HAND.L
            left_hand_parent_bone = armature.data.edit_bones.get("TAR-HAND.L")
            left_finger_bones = ["CTRL-FINGER-A-01.L", "CTRL-FINGER-B-01.L", "CTRL-FINGER-C-01.L", "CTRL-FINGER-D-01.L", "CTRL-FINGER-E-01.L"]

            if left_hand_parent_bone:
                for bone_name in left_finger_bones:
                    finger_bone = armature.data.edit_bones.get(bone_name)
                    if finger_bone:
                        finger_bone.parent = left_hand_parent_bone

            # Parentare le ossa destre a TAR-HAND.R
            right_hand_parent_bone = armature.data.edit_bones.get("TAR-HAND.R")
            right_finger_bones = ["CTRL-FINGER-A-01.R", "CTRL-FINGER-B-01.R", "CTRL-FINGER-C-01.R", "CTRL-FINGER-D-01.R", "CTRL-FINGER-E-01.R"]

            if right_hand_parent_bone:
                for bone_name in right_finger_bones:
                    finger_bone = armature.data.edit_bones.get(bone_name)
                    if finger_bone:
                        finger_bone.parent = right_hand_parent_bone



                    armature = context.object
                if armature and armature.type == "ARMATURE":
                    bpy.ops.object.mode_set(mode="POSE")

                    try:
                        preferences_bone = armature.pose.bones.get("PREFERENCES")
                        if preferences_bone:
                            # Aggiungi la proprietà personalizzata "Hand_control_ON/OFF"
                            preferences_bone["Hand_control_ON/OFF"] = 1.0
                            hand_control_prop = preferences_bone.id_properties_ui("Hand_control_ON/OFF")
                            hand_control_prop.update(min=0.0, max=1.0, description="Control whether the hand controls are active or not.")
                    except Exception as e:
                        print(f"Error adding custom property: {e}")

                    # Ossa con copy rotation
                    finger_bones_copy_rotation = [
                        "TAR-FINGER-E-02.L", "TAR-FINGER-D-02.L", "TAR-FINGER-C-02.L", "TAR-FINGER-B-02.L", "TAR-FINGER-A-02.L",
                        "TAR-FINGER-E-03.L", "TAR-FINGER-D-03.L", "TAR-FINGER-C-03.L", "TAR-FINGER-B-03.L", "TAR-FINGER-A-03.L",
                        "TAR-FINGER-E-02.R", "TAR-FINGER-D-02.R", "TAR-FINGER-C-02.R", "TAR-FINGER-B-02.R", "TAR-FINGER-A-02.R",
                        "TAR-FINGER-E-03.R", "TAR-FINGER-D-03.R", "TAR-FINGER-C-03.R", "TAR-FINGER-B-03.R", "TAR-FINGER-A-03.R"
                    ]

                    # Ossa con copy transform
                    finger_bones_copy_transform = [
                        "TAR-FINGER-A-01.R", "TAR-FINGER-B-01.R", "TAR-FINGER-C-01.R", "TAR-FINGER-D-01.R", "TAR-FINGER-E-01.R",
                        "TAR-FINGER-A-01.L", "TAR-FINGER-B-01.L", "TAR-FINGER-C-01.L", "TAR-FINGER-D-01.L", "TAR-FINGER-E-01.L"
                    ]

                    # Imposta il driver per le ossa con copy rotation
                    for bone_name in finger_bones_copy_rotation:
                        try:
                            bone = armature.pose.bones.get(bone_name)
                            if bone:
                                for constraint in bone.constraints:
                                    if constraint.type == "COPY_ROTATION":
                                        fcurve = constraint.driver_add("influence")
                                        driver = fcurve.driver
                                        driver.type = "AVERAGE"
                                        var = driver.variables.new()
                                        var.name = "HandControl"
                                        var.type = "SINGLE_PROP"
                                        target = var.targets[0]
                                        target.id = armature
                                        target.data_path = 'pose.bones["PREFERENCES"]["Hand_control_ON/OFF"]'
                                        constraint.influence = 0.0
                        except Exception as e:
                            print(f"Error setting up driver for {bone_name}: {e}")

                    # Imposta il driver per le ossa con copy transform
                    for bone_name in finger_bones_copy_transform:
                        try:
                            bone = armature.pose.bones.get(bone_name)
                            if bone:
                                for constraint in bone.constraints:
                                    if constraint.type == "COPY_TRANSFORMS":
                                        fcurve = constraint.driver_add("influence")
                                        driver = fcurve.driver
                                        driver.type = "AVERAGE"
                                        var = driver.variables.new()
                                        var.name = "HandControl"
                                        var.type = "SINGLE_PROP"
                                        target = var.targets[0]
                                        target.id = armature
                                        target.data_path = 'pose.bones["PREFERENCES"]["Hand_control_ON/OFF"]'
                                        constraint.influence = 0.0
                        except Exception as e:
                            print(f"Error setting up driver for {bone_name}: {e}")

                    bpy.ops.object.mode_set(mode="OBJECT")
                    self.report({"INFO"}, "Hand control setup completed successfully.")
                else:
                    self.report({"WARNING"}, "Please select an armature.")
                    return {"CANCELLED"}

                return {"FINISHED"}

            bpy.ops.object.mode_set(mode="OBJECT")
            self.report({"INFO"}, "Fingers Constraint setup completed successfully.")
        else:
            self.report({"WARNING"}, "Please select an armature.")
            return {"CANCELLED"}

        return {"FINISHED"}


########################################

class ORGANIZE_ARMATURE_OT_Operator(bpy.types.Operator):
    bl_idname = "object.organize_armature"
    bl_label = "Organize Armature"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # Vai in modalità Pose
        bpy.ops.object.mode_set(mode='POSE')

        # Ottieni l'oggetto armatura attivo
        armature = context.object.data

        # Funzione per creare o ottenere una Bone Collection
        def get_or_create_collection(name):
            if name not in armature.collections:
                return armature.collections.new(name)
            return armature.collections[name]

        # Crea o ottieni le Bone Collections
        mch_collection = get_or_create_collection("MCH")
        left_arm_collection = get_or_create_collection("LEFT ARM")
        left_leg_collection = get_or_create_collection("LEFT LEG")
        right_leg_collection = get_or_create_collection("RIGHT LEG")
        torso_collection = get_or_create_collection("TORSO")
        torso_tweak_collection = get_or_create_collection("TORSO_TWEAK")
        head_collection = get_or_create_collection("HEAD")
        mouth_collection = get_or_create_collection("MOUTH")
        eyes_collection = get_or_create_collection("EYES")

        # Definisci le ossa per ogni gruppo
        mch_bones = [
            "MCH-IK-ARM.L",
            "MCH-IK-FOREARM.L",
            "TAR-ARM.L",
            "TAR-FOREARM.L",
            "TAR-HAND.L",
            "MCH-CONST-ARM-FOLLOW.L",
            "MCH-ARM-FOLLOW.L",
            "MCH-IK-ARM.R",
            "MCH-IK-FOREARM.R",
            "TAR-ARM.R",
            "TAR-FOREARM.R",
            "TAR-HAND.R",
            "MCH-CONST-ARM-FOLLOW.R",
            "MCH-ARM-FOLLOW.R",
            "MCH-IK-LEG.R",
            "MCH-IK-SHIN.R",
            "TAR-SHIN.R",
            "TAR-LEG.R",
            "TAR-TOE.R",
            "TAR-FOOT.R",
            "MCH-B-ROLL-O1-FEET.R",
            "MCH-B-ROLL-O2-FEET.R",
            "MCH-IK-LEG.L",
            "MCH-IK-SHIN.L",
            "TAR-SHIN.L",
            "TAR-LEG.L",
            "TAR-TOE.L",
            "TAR-FOOT.L",
            "MCH-B-ROLL-O1-FEET.L",
            "MCH-B-ROLL-O2-FEET.L",
            "MCH-EYE.R",
            "MCH-INT-TARGET-EYES",
            "MCH-TARGET-EYES",
            "MCH-EYE.L"
        ]
        
        left_arm_bones = [
            "CTRL-ROLL-ELBOW.L",
            "CTRL-IK-ARM.L",
            "MCH-IK-HAND.L",
            "CTRL-FK-ARM.L",
            "CTRL-FK-FOREARM.L"
        ]

        left_leg_bones = [
            "MCH-IK-TOE.L",
            "CTRL-B-FOOT.L",
            "CTRL-ROLL-FOOT.L",
            "CTRL-FK-LEG.L",
            "CTRL-FK-SHIN.L",
            "CTRL-FK-FOOT.L",
            "CTRL-FK-TOE.L"
        ]

        right_leg_bones = [
            "CTRL-FK-LEG.R",
            "CTRL-FK-SHIN.R",
            "CTRL-FK-FOOT.R",
            "CTRL-FK-TOE.R",  # Ho corretto il nome da CTRL-FK-TOE.L a CTRL-FK-TOE.R
            "MCH-IK-TOE.R",
            "CTRL-B-FOOT.R",
            "CTRL-ROLL-FOOT.R"
        ]

        torso_bones = [
            "TAR-HIPS",
            "TAR-UPPER BODY",
            "CTRL-CHEST",
            "TAR-SHOULDER.R",
            "TAR-SHOULDER.L"
        ]

        torso_tweak_bones = [
            "TAR-SPINE-02",
            "TAR-SPINE",
            "TAR-CHEST"
        ]

        head_bones = [
            "TAR-HEAD",
            "TAR-NECK",
            "TAR-UPPER_JAW",
            "TAR-JAW"
        ]

        mouth_bones = [
            "TAR-TONGUE-01",
            "TAR-TONGUE-02",
            "TAR-TONGUE-03",
            "TAR-UPPER-TEETH",
            "TAR-LOWER-TEETH"
        ]

        eyes_bones = [
            "TAR-INFERIOR-EYELID.R",
            "TAR-UPPER-EYELID.R",
            "TAR-EYE.R",
            "MCH-EYE.R",
            "MCH-TARGET-EYE.R",
            "MCH-TARGET-EYE.L",
            "MCH-TARGET-EYES",
            "TAR-UPPER-EYELID.L",
            "TAR-INFERIOR-EYELID.L",
            "TAR-EYE.L"
        ]

        # Assegna le ossa alle rispettive collezioni
        def assign_bones_to_collection(bones, collection):
            for bone_name in bones:
                if bone_name in armature.bones:
                    bone = armature.bones[bone_name]
                    collection.assign(bone)

        assign_bones_to_collection(mch_bones, mch_collection)
        assign_bones_to_collection(left_arm_bones, left_arm_collection)
        assign_bones_to_collection(left_leg_bones, left_leg_collection)
        assign_bones_to_collection(right_leg_bones, right_leg_collection)
        assign_bones_to_collection(torso_bones, torso_collection)
        assign_bones_to_collection(torso_tweak_bones, torso_tweak_collection)
        assign_bones_to_collection(head_bones, head_collection)
        assign_bones_to_collection(mouth_bones, mouth_collection)
        assign_bones_to_collection(eyes_bones, eyes_collection)

        bpy.ops.object.mode_set(mode="OBJECT")  # Torna in modalità Object
        self.report({"INFO"}, "Bones compilation")

        return {'FINISHED'}
"""
class MAKE_CUSTOM_ARMATURE_OT_Operator(bpy.types.Operator):
    bl_idname = "object.make_custom_armature"
    bl_label = "Make Custom Armature"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # Ottieni il percorso del file corrente e costruisci il percorso relativo a bones_geometry.blend
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(current_dir, "bones_geometry.blend")

        # Controlla se il file esiste
        if not os.path.exists(filepath):
            self.report({'ERROR'}, f"File not found: {filepath}")
            return {'CANCELLED'}

        # Append the necessary objects from the file
        meshes_to_load = ["ik_circle", "chest", "root", "ctrl_eyes", "eye_aim"]
        loaded_meshes = {}

        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            data_to.objects = [name for name in meshes_to_load if name in data_from.objects]

        for obj in data_to.objects:
            if obj is not None:
                loaded_meshes[obj.name] = obj

        def assign_custom_shape(bone_name, mesh_name, scale, translation, rotation):
            if bone_name in armature.pose.bones:
                bone = armature.pose.bones[bone_name]
                bone.custom_shape = loaded_meshes.get(mesh_name)
                bone.custom_shape_scale_xyz = scale
                bone.custom_shape_translation = translation
                bone.custom_shape_rotation_euler = rotation

        # Ottieni l'oggetto armatura attivo
        armature = context.object

        # Assegna le geometrie personalizzate alle ossa specificate
        assign_custom_shape("CTRL-KNEE-ROLL.L", "ik_circle", (0.4, 0.4, 0.4), (0.0, 0.0, 0.0), (1.5708, 0, 1.5708))
        assign_custom_shape("CTRL-KNEE-ROLL.R", "ik_circle", (0.4, 0.4, 0.4), (0.0, 0.0, 0.0), (1.5708, 0, 1.5708))

        assign_custom_shape("TAR-CHEST", "chest", (1.9, 0.9, 1.6), (0.0, 0.12, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("TAR-SPINE", "chest", (2.4, 0.4, 2.1), (0.0, 0.05, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("TAR-SPINE-02", "chest", (3.0, 0.4, 2.8), (0.0, 0.05, 0.0), (0.0, 0.0, 0.0))

        assign_custom_shape("root", "root", (0.6, 0.6, 0.6), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

        assign_custom_shape("CTRL-TARGET-EYES", "ctrl_eyes", (0.4, 0.4, 0.4), (0.0, 0.0, 0.0), (1.5708, 0.0, 0.0))
        assign_custom_shape("MCH-TARGET-EYE.R", "eye_aim", (1.0, 2.0, 2.0), (0.0, 0.009, 0.0), (0.0, 0.0, 1.5708))
        assign_custom_shape("MCH-TARGET-EYE.L", "eye_aim", (1.0, 2.0, 2.0), (0.0, 0.009, 0.0), (0.0, 0.0, 1.5708))


        assign_custom_shape("root", "root", (0.6, 0.6, 0.6), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("root", "root", (0.6, 0.6, 0.6), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("root", "root", (0.6, 0.6, 0.6), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
        

        return {'FINISHED'}

"""

class MAKE_CUSTOM_ARMATURE_OT_Operator(bpy.types.Operator):
    bl_idname = "object.make_custom_armature"
    bl_label = "Make Custom Armature"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # Ottieni il percorso del file corrente e costruisci il percorso relativo a bones_geometry.blend
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(current_dir, "bones_geometry.blend")

        # Controlla se il file esiste
        if not os.path.exists(filepath):
            self.report({'ERROR'}, f"File not found: {filepath}")
            return {'CANCELLED'}

        # Funzione per appendere l'oggetto dal file .blend
        def append_object_from_blend(filepath, object_name):
            with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
                if object_name in data_from.objects:
                    data_to.objects = [object_name]
            return data_to.objects[0]

        # Append the necessary objects
        ik_circle = append_object_from_blend(filepath, "ik_circle")
        chest = append_object_from_blend(filepath, "chest")
        root = append_object_from_blend(filepath, "root")
        ctrl_eyes = append_object_from_blend(filepath, "ctrl_eyes")
        eye_aim = append_object_from_blend(filepath, "eye_aim")
        shoulder = append_object_from_blend(filepath, "shoulder")
        gear = append_object_from_blend(filepath, "gear")
        rectangle = append_object_from_blend(filepath, "rectangle")
        circle = append_object_from_blend(filepath, "circle")
        circles = append_object_from_blend(filepath, "circles")
        triquad = append_object_from_blend(filepath, "triquad")
        triangle = append_object_from_blend(filepath, "triangle")
        rectanglecube = append_object_from_blend(filepath, "rectanglecube")
        finger_rect = append_object_from_blend(filepath, "finger_rect")
        text = append_object_from_blend(filepath, "P")

        def assign_custom_shape(bone_name, mesh, scale, translation, rotation):
            if bone_name in armature.pose.bones:
                bone = armature.pose.bones[bone_name]
                bone.custom_shape = mesh
                bone.custom_shape_scale_xyz = scale
                bone.custom_shape_translation = translation
                bone.custom_shape_rotation_euler = rotation

        # Ottieni l'oggetto armatura attivo
        armature = context.object

        # Assegna le geometrie personalizzate alle ossa specificate
        assign_custom_shape("CTRL-KNEE-ROLL.L", ik_circle, (0.4, 0.4, 0.4), (0.0, 0.0, 0.0), (1.5708, 0, 1.5708))
        assign_custom_shape("CTRL-KNEE-ROLL.R", ik_circle, (0.4, 0.4, 0.4), (0.0, 0.0, 0.0), (1.5708, 0, 1.5708))

        assign_custom_shape("TAR-CHEST", chest, (1.9, 0.9, 1.6), (0.0, 0.12, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("TAR-SPINE", chest, (2.4, 0.4, 2.1), (0.0, 0.05, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("TAR-SPINE-02", chest, (3.0, 0.4, 2.8), (0.0, 0.05, 0.0), (0.0, 0.0, 0.0))

        assign_custom_shape("root", root, (0.6, 0.6, 0.6), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

        assign_custom_shape("CTRL-TARGET-EYES", ctrl_eyes, (0.4, 0.4, 0.4), (0.0, 0.0, 0.0), (1.5708, 0.0, 0.0))
        assign_custom_shape("MCH-TARGET-EYE.R", eye_aim, (1.0, 2.0, 2.0), (0.0, 0.009, 0.0), (0.0, 0.0, 1.5708))
        assign_custom_shape("MCH-TARGET-EYE.L", eye_aim, (1.0, 2.0, 2.0), (0.0, 0.009, 0.0), (0.0, 0.0, 1.5708))

        assign_custom_shape("TAR-SHOULDER.L", shoulder, (1, 1, 1), (0.0, 0.055, 0.0), (0.0, 0.0, 0.0))
        assign_custom_shape("TAR-SHOULDER.R", shoulder, (1, 1, 1), (0.0, 0.055, 0.0), (0.0, 0.0, 0.0))


        assign_custom_shape("CTRL-ROLL-ELBOW.L", ik_circle, (1, 1, 1), (0.0, 0.0, 0.0), (1.5708, 0, 1.5708))
        assign_custom_shape("CTRL-ROLL-ELBOW.R", ik_circle, (1, 1, 1), (0.0, 0.0, 0.0), (1.5708, 0, 1.5708))

        assign_custom_shape("CTRL-ROLL-FOOT.L", gear, (0.3, 0.3, 0.3), (0.0, 0.06, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-ROLL-FOOT.R", gear, (0.3, 0.3, 0.3), (0.0, 0.06, 0.0), (1.5708, 0, 0))


        assign_custom_shape("CTRL-CHEST", rectangle, (1.3, 1.3, 1.3), (0.0, 0.05, 0.0), (1.5708, 0, 0))
        assign_custom_shape("TAR-UPPER BODY", rectangle, (3.2, 3.2, 2.6), (0.0, 0.0, 0.0), (0, 0, 0))
        assign_custom_shape("TAR-HIPS", rectangle, (1.9, 1, 1), (0.0, 0.05, 0.0), (1.5708, 0, 0))

        assign_custom_shape("TAR-HEAD", chest, (1, 1.1, 1.3), (-0.01, 0.13, 0.0), (0, 1.5708, 0))
        assign_custom_shape("TAR-NECK", circle, (2.2, 2.2, 2.2), (-0.01, 0.13, 0.0), (1.5708, 0, 0))

        assign_custom_shape("CTRL-FK-ARM.L", circles, (0.25, 0.25, 0.3), (0, 0.07, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-FK-ARM.R", circles, (0.25, 0.25, 0.3), (0, 0.07, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-FK-LEG.L", circles, (0.2, 0.2, 0.2), (0, 0.23, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-FK-LEG.R", circles, (0.2, 0.2, 0.2), (0, 0.23, 0.0), (1.5708, 0, 0))


        assign_custom_shape("CTRL-FK-SHIN.L", triquad, (0.4, 0.4, 0.6), (0, 0.32, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-FK-SHIN.R", triquad, (0.4, 0.4, 0.6), (0, 0.32, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-FK-FOREARM.L", triquad, (0.4, 0.4, 0.9), (0, 0.18, 0.0), (1.5708, 0, 0))
        assign_custom_shape("CTRL-FK-FOREARM.R", triquad, (0.4, 0.4, 0.9), (0, 0.18, 0.0), (1.5708, 0, 0))

        assign_custom_shape("MCH-IK-TOE.L", triangle, (0.3, 0.3, 0.3), (0, 0.04, 0.0), (0, 1.5708, 0))
        assign_custom_shape("MCH-IK-TOE.R", triangle, (0.3, 0.3, 0.3), (0, 0.04, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FK-TOE.L", triangle, (0.3, 0.3, 0.3), (0, 0.04, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FK-TOE.R", triangle, (0.3, 0.3, 0.3), (0, 0.04, 0.0), (0, 1.5708, 0))

        assign_custom_shape("MCH-IK-HAND.L", triangle, (0.7, 0.7, 0.7), (0, 0.035, 0.0), (0, 1.5708, 0))
        assign_custom_shape("MCH-IK-HAND.R", triangle, (0.7, 0.7, 0.7), (0, 0.035, 0.0), (0, 1.5708, 0))

        assign_custom_shape("CTRL-B-FOOT.L", rectanglecube, (0.2, 0.35, 0.1), (0, 0.07, 0.0), (0, 0, 0))
        assign_custom_shape("CTRL-B-FOOT.R", rectanglecube, (0.2, 0.35, 0.1), (0, 0.07, 0.0), (0, 0, 0))
        assign_custom_shape("CTRL-FK-FOOT.L", rectanglecube, (0.2, 0.35, 0.1), (0, 0.07, 0.0), (0, 0, 0))
        assign_custom_shape("CTRL-FK-FOOT.R", rectanglecube, (0.2, 0.35, 0.1), (0, 0.07, 0.0), (0, 0, 0))
        

        assign_custom_shape("CTRL-FINGER-A-01.L", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-B-01.L", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-C-01.L", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-D-01.L", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-E-01.L", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-A-01.R", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-B-01.R", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-C-01.R", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-D-01.R", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-E-01.R", finger_rect, (0.2, 0.45, 0.3), (0, 0.0, 0.0), (0, 1.5708, 0))

        assign_custom_shape("CTRL-FINGER-A-02.L", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-B-02.L", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-C-02.L", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-D-02.L", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-E-02.L", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-A-02.R", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-B-02.R", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-C-02.R", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-D-02.R", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-FINGER-E-02.R", finger_rect, (0.2, 0.35, 0.7), (0, 0.005, 0.0), (0, 1.5708, 0))

        assign_custom_shape("CTRL-IK-ARM.L", finger_rect, (1, 0.4, 0.3), (0, 0.03, 0.0), (0, 1.5708, 0))
        assign_custom_shape("CTRL-IK-ARM.R", finger_rect, (1, 0.4, 0.3), (0, 0.03, 0.0), (0, 1.5708, 0))

        assign_custom_shape("PREFERENCES", text, (5, 5, 5), (0, 0.0, 0.0), (0, 0, 0))


        return {'FINISHED'}




class RIG_PROPERTIES_PT_Panel(bpy.types.Panel):
    bl_label = "Rig Properties"
    bl_idname = "VIEW3D_PT_rig_properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        armature = context.object
        if armature and armature.type == 'ARMATURE' and context.mode == 'POSE':
            preferences_bone = armature.pose.bones.get("PREFERENCES")
            if preferences_bone:
                for prop_name in preferences_bone.keys():
                    if prop_name not in preferences_bone['_RNA_UI']:
                        continue
                    row = layout.row()
                    row.prop(preferences_bone, f'["{prop_name}"]', text=prop_name)
            else:
                layout.label(text="Bone 'PREFERENCES' not found.")
        else:
            layout.label(text="No armature selected or not in Pose Mode.")


class RENAME_BONES_PT_Panel(bpy.types.Panel):
    bl_label = "Rigging Tools"
    bl_idname = "VIEW3D_PT_rigging_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        # Crea un box espandibile per i controlli
        box = layout.box()
        row = box.row()
        row.prop(context.scene, "show_rigging_tools", icon="TRIA_DOWN" if context.scene.show_rigging_tools else "TRIA_RIGHT", icon_only=True, emboss=False)
        row.label(text="Rigging Tools")

        if context.scene.show_rigging_tools:
            box.operator("object.rename_bones")
            box.operator("object.arrange_bones")
            box.operator("object.create_mch_bones", text="Create MCH")
            box.operator("object.make_ctrl_bones", text="Make CTRL bones")
            box.operator("object.apply_constraint", text="Apply Constraint")
            
            # Crea un altro box espandibile per i controlli personalizzati
            custom_box = layout.box()
            row = custom_box.row()
            row.prop(context.scene, "show_custom_armature", icon="TRIA_DOWN" if context.scene.show_custom_armature else "TRIA_RIGHT", icon_only=True, emboss=False)
            row.label(text="Custom Armature")

            if context.scene.show_custom_armature:
                custom_box.operator("object.organize_armature", text="Organize Armature")
                custom_box.operator("object.make_custom_armature", text="Make Custom Armature")


class RigPropertiesPanel(bpy.types.Panel):
    bl_label = "Rig Properties"
    bl_idname = "VIEW3D_PT_rig_properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Properties Bone"

    @classmethod
    def poll(cls, context):
        return context.mode == 'POSE' and context.object is not None and context.object.type == 'ARMATURE'

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj and obj.type == 'ARMATURE':
            bone = obj.pose.bones.get("PREFERENCES")
            if bone:
                for key in bone.keys():
                    if key != "_RNA_UI":
                        row = layout.row()
                        row.prop(bone, f'["{key}"]')

def register():
    bpy.utils.register_class(RENAME_BONES_PT_Panel)
    bpy.utils.register_class(RENAME_BONES_OT_Rename)
    bpy.utils.register_class(ARRANGE_BONES_OT_Arrange)
    bpy.utils.register_class(CREATE_MCH_BONES_OT_CreateMCH)
    bpy.utils.register_class(MAKE_CTRL_BONES_OT_CreateCtrlBones)
    bpy.utils.register_class(RigPropertiesPanel)
    
    # Registra gli operatori personalizzati
    bpy.utils.register_class(ORGANIZE_ARMATURE_OT_Operator)
    bpy.utils.register_class(MAKE_CUSTOM_ARMATURE_OT_Operator)

    # Aggiungi le proprietà boolean per mostrare/nascondere i box
    bpy.types.Scene.show_rigging_tools = bpy.props.BoolProperty(name="Show Rigging Tools", default=True)
    bpy.types.Scene.show_custom_armature = bpy.props.BoolProperty(name="Show Custom Armature", default=False)

def unregister():
    bpy.utils.unregister_class(RENAME_BONES_PT_Panel)
    bpy.utils.unregister_class(RENAME_BONES_OT_Rename)
    bpy.utils.unregister_class(ARRANGE_BONES_OT_Arrange)
    bpy.utils.unregister_class(CREATE_MCH_BONES_OT_CreateMCH)
    bpy.utils.unregister_class(MAKE_CTRL_BONES_OT_CreateCtrlBones)
    bpy.utils.unregister_class(RigPropertiesPanel)
    
    # Deregistra gli operatori personalizzati
    bpy.utils.unregister_class(ORGANIZE_ARMATURE_OT_Operator)
    bpy.utils.unregister_class(MAKE_CUSTOM_ARMATURE_OT_Operator)

    # Rimuovi le proprietà boolean
    del bpy.types.Scene.show_rigging_tools
    del bpy.types.Scene.show_custom_armature

if __name__ == "__main__":
    register()
    