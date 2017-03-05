import flash_cards as fc
lbb_notes="""The long head of the Biceps Brachii originates via a
tendon, half of the fibers attach to the supraglenoid tubercle and
the other half to the superior glenoid labrum (mainly its posterior
part). From its origin, this tendon passes throuigh the capsule of
the shoulder joint and emerges into the intertubercular sulcus of the
humerus.

The long and short heads join and give rise to a tendon that inserts
into the medial and posterior surfaces of the radial tuberosity; the
tendon sends an expansion (bicipital aponeurosis) medially into the
deep fascia of the proximal forearm.

Is used as a flexor when strength of brachialis is insufficient for the
desired speed or effort; because biceps also supinates, its use as a
flexor is greater when supination of the forearm is acceptable than
when the forearm must be kept pronated."""
long_biceps_brachii=fc.Muscle(
    "Long Head of Biceps Brachii", "Supraglenoid Tubercle and Superior Glenoid
    Labrum of the Scapula", "Radial Tuberosity", "Flexes and Supinates 
    Forearm", "Musculocutaneous Nerve", lbb_notes)
sbb_notes="""The short head of the Biceps Brachii originates on the coracoid process of the scapula (in common with coracobrachialis).

The long and short heads join and give rise to a tendon that inserts into the medial and posterior surfaces of the radial tuberosity;
the tendon sends an expansion (bicipital aponeurosis) medially into the depp fascia of the proximal forearm.

Is used as a flexor when strength of brachialis is insufficient for the desired speed or effort;
because biceps also supinates, its use as a flexor is greater when supination of the forearm is acceptable
than when the forearm must be kept pronated;
short head also adducts arm weakly."""
short_biceps_brachii=fc.Muscle("Short Head of Biceps Brachii", ("Scapula", "Coracoid Process"), ("Radius", "Radial Tuberosity"), ["Flexes Forearm", "Supinates Forearm", "Adduct Arm"], "Musculocutaneous Nerve", sbb_notes)
brach_notes="""Originates from the lateral surface of the humeral shaft behind the lower part of the deltoid tuberosity;
lateral, anterior, and medial surfaces of the shaft below this tuberosity.

Inserts on the anterior aspect of the coronoid process of the Ulna and the ulnar tuberosity.

Is always used during active flexion of the forearm because it is the only muscle that does this purely.

Innervated by the Musculocutaneous Nerve (and, usually, the radial n. to distolateral part of the muscle)."""
brachialis=fc.Muscle("Brachialis", ("Humerus", "Humeral Shaft Below Deltoid Tuberosity"), ("Ulna", "Coronoid Process and Ulnar Tuberosity"), ["Flexes Forearm"], ["Musculocutaneous Nerve", "Radial Nerve"], brach_notes)
trap_notes="""The Trapezius originates from the medialmost part of the superior nuchal line,
the nuchal ligament, and the thoracic vertebral spines.

It inserts on the lateral third of the clavicle, the medial edge of the acromion,
the superior lip of the crest of the scapular spine, and the tubercle of the scapular spine.

Upper fibers elevate the shoulder girdle, as in a shrug and during arm elevation.
Middle fibers retraact the scapula.
Lower fibers depress the scapula; they also participate in glenoid-up rotation during abduction of the arm.

It is innervated by the Accessory Nerve and C3-4 Ventral rami."""
trapezius=fc.Muscle("Trapezius", ("Vertebrae","Cervical and Thoracic Spines and Nuchal Ligament"),("Clavicle and Scapula", "Lateral third of clavicle, medial edge of acromion, superior lip of the crest of the scapular spine, and the tubercle of the scapular spine"),["Elevates Pectoral Girdle", "Retracts Scapula", "Depresses Scapula", "Glenoid Up Rotation of Scapula"],["Accessory Nerve", "C3-C4 Ventral Rami"], trap_notes)
serr_ant_notes="""The Serratus Anterior originates as digitations from the upper nine ribs.

The upper two digitations insert on the ventral surface of the vertebral bordal of the scapula.
The lower seven digitations converge on the ventral surface of the inferior angle of the scapula.

The upper digitations protract and elevate the scapula. The lower digitations pull the inferior angle forward,
thereby contributing to protraction and serving as a major glenoid-up rotator, but used more during flexion
of the arm than during abduction.

It is innervated by the Long Thoracic Nerve (C5-C7 ventral rami)."""
serratus_anterior=fc.Muscle("Serratus Anterior", ("Ribs", "Upper Nine"), ("Scapula", "Ventral Surface of Vertebral Border and Inferior Angle"), ["Protracts and Elevates Scapula", "Glenoid Up Rotation of Scapula"], "Long Thoracic Nerve", serr_ant_notes)
spinalis_notes="""Spinalis originates and inserts on the vertebral spines.

Its action is so small as to be mechanically insignificant.

It is flimsy, highly tendinous, and usually only occupies the thoracic region.

Spinalis, Longissimus, and Iliocostalis, collectively form the Erector Spinae mm. They are innervated by dorsal rami of spinal nerves."""
spinalis=fc.Muscle("Spinalis", ("Vertebrae", "Spines"), ("Vertebrae", "Spines"), "Mechanically Insignificant", "Dorsal Rami of Spinal Nerves", spinalis_notes)
longissimus_notes="""Longissimus originates aponeurotically from the sacrum and from transverse elements of presacral vertebrae.

It inserts on transverse and costal elements of vertebrae near their junction; the most superior fibers insert onto the mastoid
process of the skull and are called Longissimus Capitis.

Acting bilaterally, Longissimus is an extensor of the vertebral column. Acting unilaterally, it laterally flexes the vertebral column.

It lies lateral to the Spinalis.

Spinalis, Longissimus, and Iliocostalis, collectively form the Erector Spinae mm. They are innervated by dorsal rami of spinal nerves."""
longissimus=fc.Muscle("Longissimus", "Aponeurotically from Sacrum and from Transverse Elements of Presacral Vertebrae", "Transverse and Costal Elements of Vertebrae and the Mastoid Process", ["Extends Vertebral Column", "Laterally Flexes Vertebral Column"], "Dorsal Rami of Spinal Nerves", longissimus_notes)
iliocostalis_notes="""Iliocostalis originates aporneurotically from the sacrum and adjacent part of the iliac crest. Higher up, it originates from the
ribs near their angles.

It inserts on the ribs near their angles; the most superior fibers insert onto posterior tubercles of cervical vertebrae.

Acting bilaterally, Iliocostalis is an extensor of the vertebral column. Unilaterally, it is a strong lateral flexor of the spine.

It lies lateral to the Longissimus.

Spinalis, Longissimus, and Iliocostalis, collectively form the Erector Spinae mm. They are innervated by dorsal rami of spinal nerves."""
iliocostalis=fc.Muscle("Iliocostalis", "Aponeurotically from Sacrum and Iliac Crest, and from Ribs near their Angles", "Ribs near their Angles and Posterior Tubercles of Cervical Vertebrae", ["Extends Vertebral Column", "Laterally Flexes Vertebral Column"], "Dorsal Rami of Spinal Nerves", iliocostalis_notes)
tvspl_notes="""The Transversospinal Muscles are Semispinalis, Multifidus, and Rotatores.

They originate from the transverse elements of vertebrae and insert on the vertebral spines.

Acting bilaterally, they contribute to extension of the vertebral column. Acting unilaterally, they laterally flex the spine and (if the intervertebral joints permit)
axially rotate the vertebral column toward the opposite side.

They lie deep to Erector Spinae and are innervated by dorsal rami of spinal nerves."""
semispinalis_notes="""Semispinalis is the most superficial of the Transversospinal Muscles. It is absent in the lumbar and sacral regions and each bundle spans 4-6 vertebrae.

The superior-most portion of Semispinalis, called Semispinalis Capitis, originates from the transverse elements of upper thoracic and lower cervical vertebrae.

Semispinalis Capitis inserts on the nuchal plane of the occipital bone near the midline.

Semispinalis Capitis powerfully extends the head.

It lies in the space immediately lateral to the nuchal ligament, deep to Splenius Capitis and Trapezius."""
semispinalis_capitis=fc.Muscle("Semispinalis Capitis", "Transverse Elements of Upper Thoracic and Lower Cervical Vertebrae", "Mastoid Process and Lateral Half of Superior Nuchal Line", "Powerfully Extends the Head", "Dorsal Rami of Spinal Nerves",tvspl_notes+"\n\n"+semispinalis_notes)
multifidus_notes="""The lowest fibers of Multifidus also gain an origin from the posterior end of the iliac crest.

Multifidus is the most powerful of the Transversospinal Muscles and is the only one to exist thoughout the whole length of the vertebral column.
It lies deep to Semispinalis where they coexist. Each bundle spans 2-4 vertebrae."""
mutifidus=fc.Muscle("Multifidus", "Transverse Elements of Vertebrae and the Posterior end of the Iliac Crest", "Vertebral Spines", "Extension and Lateral Flexion of the Vertebral Column", "Dorsal Rami of Spinal Nerves",tvspl_notes+"\n\n"+multifidus_notes)
rotatores_notes="""Rotatores is the smallest and deepest of the Transversospinal Muscles. It is well developed only in the thoracic region.
Each bundle spans 1-2 vertebrae."""
rotatores=fc.Muscle("Rotatores", "Transverse Elements of Vertebrae", "Vertebral Spines", "Extends and Laterally Flexes Vertebral Column", "Dorsal Rami of Spinal Nerves", tvspl_notes+"\n\n"+rotatores_notes)
splenius_notes="""Splenius originates from the spines of upper thoracic vertebrae and the lower part of the nuchal ligament.

It is divided into Splenius Capitis and Splenius Cervicis based on its insertion. Splenius Capitis inserts on the mastoid process and lateral half of the superior nuchal line.
Splenius Cervicis inserts on the posterior bars of the cervical transverse processes.

It extends the head and neck and rotates the head towards the ipsilateral side.

It is innervated by dorsal rami of spinal nerves."""
splenius=fc.Muscle("Splenius", "Spines of Upper Thoracic Vertebrae", "(Capitis) Inserts on the Mastoid Process and the Lateral Half of the Superior Nuchal Line; (Cervicis) Inserts on the Posterior Bars of the Cervical Transverse Processes", "Extends the Head and Neck and Rotates the Head Towards the Ipsilateral Side", "Dorsal Rami of Spinal Nerves",splenius_notes)
suboccipital_notes="""The Suboccipital Muscles includes: Rectus Capitis Posterior Major, Rectus Capitis Posterior Minor, Obliquus Capitis Inferior,
and Obliquus Capitis Superior. These muscles connect the atlas to the axis, or connect one of these bones to the skull.

Some extend the head at the atlanto-occipital joint, other rotate the head at the atlanto-axial joint.

All of these muscles lie deep to the Semispinalis Capitis.

They are innervated by dorsal rami of spinal nerves."""
suboccipital_muscles=fc.Muscle("Suboccipital Muscles: Rectus Capitis Posterior Major, Rectus Capitis Posterior Minor, Obliquus Capitis Inferior, and Obliquus Capitis Superior", "Connect Atlas, Axis, and Skull", "Connect Atlas, Axis, and Skull", "Extend Head at Atlanto-Occipital Joint, Rotate Head at Atlanto-Axial Joint", "Dorsal Rami of Spinal Nerves", suboccipital_notes)
intercostal_notes="""Each of the 11 intercostal spaces is occupied by three layers of intercostal muscle: external, internal, and innermost. The fibers of the external
intercostal muscle run at right angles to those of the internal intercostal muscle, which run in the same direction as the innermost muscle fibers. Anteriorly, 
the innermost layer is replaced by the transversus thoracis muscle, running from costal cartilages to sternum.

Function is unclear. Activity during respiration is remarkably limited.

Innervated by intercostal nerves."""
intercostals=fc.Muscle("Intercostal Muscles and Transversus Thoracis", "Ribs", "Ribs", "Unclear", "Intercostal Nerves", intercostal_notes)
diaphragm_notes="""The abdominal diaphragm originates on inner aspects of the xiphoid process, costal cartilages and ribs, fascia on quadratus lumborum and psoas major, and the sides
of the upper lumbar vertebrae. The bundles arising from the vertebrae are called crura.

The fibers converge towards the central tendon at the dome of the diaphragm.

It expands the thoracic cavity and compresses the abdominal cavity; functions in inspiration.

Somatic motor innervation: phrenic nerve (C3-5). Sensory: phrenic nerve for central portion, intercostal nerves for the margin."""
diaphragm=fc.Muscle("Diaphragm", "Base of Ribcage and Fascia of Quadratus Lumborum and Psoas Major", "Central Tendon", "Expands Thoracic Cavity and Compresses Abdominal Cavity", "Phrenic Nerve and Intercostal Nerves", diaphragm_notes)
EAO_notes="""External Abdominal Obliques originate on the lateral surfaces of the lower ribs.

Inserts on the anterior half of the iliac crest and, via an aponeurosis, into rectus sheath and pubic body.

Flexes and Laterally Flexes the lumbar vertebral column. Increases intra-abdominal pressure.

Innervated by intercostal nerves 7-11, the subcostal nerve (T12), and iliohypogastric and ilioinguinal nerves (L1).

Corresponds to external intercostal muscle of the thorax; inferior edge of the aponeurosis is called the inguinal ligament."""
EAO=fc.Muscle("External Abdominal Oblique", "Lateral Surface of the Lower Ribs", "Anterior Half of Iliac Crest and (via an aponeurosis) into the Rectus Sheath and Pubic Body", "Lateral Flexion and Flexion of Lumbar Vertebral Column; Increases Intra-Abdominal Pressure", "Intercostal Nerves 7-11, Subcostal Nerve (T12), Iliohypogastric and Ilioinguinal Nerves (L1)", EAO_notes)
IAO_notes="""Internal Abdominal Obliques originate on the anterior three-fifths of the iliac crest and the iliopectineal arch.

Inserts on the inferior edges of the lower ribs and, via an aponeurosis, into the rectus sheath and the pubic body.

Flexes and Laterally Flexes the lumbar vertebral column. Increases intra-abdominal pressue.

Innervated by intercostal nerves 7-11, the subcostal nerve (T12), and iliohypogastric and ilioinguinal nerves (L1).

Corresponds to internal intercostal muscle of the thorax; fibers from ASIS of the ilium run transversely, fibers from iliopectineal arch curve inferiorly."""
IAO=fc.Muscle("Internal Abdominal Oblique", "Anterior 3/5 of the Iliac Crest and the Iliopectineal Arch", "Inferior Edges of Lower Ribs and (via and aponeurosis) into the Rectus Sheath and Pubic Body", , "Lateral Flexion and Flexion of Lumbar Vertebral Column; Increases Intra-Abdominal Pressure", "Intercostal Nerves 7-11, Subcostal Nerve (T12), Iliohypogastric and Ilioinguinal Nerves (L1)", IAO_notes)
TA_notes="""Transversus Abdominis originates on the inner surfaces of the lower costal cartilages, via an aponeurosis from lumbar transverse processes,
and fleshily from anterior half of iliac crest and the iliopectineal arch.

It inserts via an aponeurosis into the rectus sheath, pubic body, and by sparse tendon fibers into the pecten pubis of the superior pubic ramus.

It increases intra-abdominal pressure.

Innervated by intercostal nerves 7-11, the subcostal nerve (T12), and iliohypogastric and ilioinguinal nerves (L1).

Corresponds to innermost intercostal muscle of the thorax; most fibers run transversely, but fibers from the iliopectineal arch curve inferiorly; 
10% of the time the tendon fibers to pecten pubis form a continuous sheet -- the falx inguinalis."""
TA=fc.Muscle("Transversus Abdominis", "Inner Surfaces of Lower Costal Cartilages (via an aponeurosis) from Lumbar Transverse Processes, and (fleshily) from the anterior half of the Iliac Crest and the Iliopectineal Arch", "(Via an aponeurosis) into Rectus Sheath, Pubic Body, and by Sparse Tendon Fibers into Pecten Pubis of Superior Pubic Ramus", "Increases Intra-Abdominal Pressure", "Intercostal Nerves 7-11, Subcostal Nerve (T12), Iliohypogastric and Ilioinguinal Nerves (L1)", TA_notes)
RA_notes="""The Rectus Abdominis originates from the Ciphoid Process and the ventral surfaces of the the lower costal cartilages.

It inserts via a short tendon onto the the pubic crest and the anterior surface of the pubic body.

It flexes the lumbar vertebral column, helps other muscles to increase intra-abdominal pressure.

It is innervated by intercostal nerves 7-11 and the subcostal nerves (T12).

The superior half of each Rectus Abdominis is interrupted by 3 or 4 tendinous intersections"""
RA=fc.Muscle("Rectus Abdominis", "Xiphoid Process and the Ventral Surfaces of Lower Costal Cartilages", "Via a Short Tendon onto the Pubic Crest and Anterior Surface of the Pubic Body", "Flexes Lumbar Vertebral Column and Helps Increase Intra-Abdominal Pressure", "Intercostal Nerves 7-11 and Subcostal Nerve (T12)", RA_notes)
pyramidalis_notes="""The Pyramidalis is absent in 20% of people. It originates from the anterior surface of the pubic body.

It inserts into the linea alba above the pubic symphysis. Its action is unknown.

It is innervated by the Subcostal Nerve (T12).

It lies on the anterior surface of the Rectus Abdominis and is a guide to the linea alba in OB/GYN surgery."""
pyramidalis=fc.Muscle("Pyramidalis", "Anterior Surface of the Pubic Body", "Into Linea Alba above Pubic Symphysis", "Unknown", "Subcostal Nerve (T12)", pyramidalis_notes)
psoas_minor_notes="""The Psoas Minor is an unimportant muscle with an uncertain action and an unimportant innervation. It is usually absent,
but when it does exist it is largely tendinous and lies on the anterior surface of Psoas Major.

It originates from the T12/L1 intervertebral disc and adjacent vertebral bodies, and it inserts on the iliopubic eminence of the os coxae.

Embryological studies show that, despite not attaching to a long bone, it is developmentally an lower limb muscle."""
psoas_minor=fc.Muscle("Psoas Minor", "T12/L1 IV Disc and Adjacent Vertebral Bodies", "Iliopubic Eminence of Os Coxae", "Unknown", "Unimportant", psoas_minor_notes)
psoas_major_notes="""Psoas Major originates from the lateral surface of the lumbar vertebral column. It combines with the Iliacus to form the
Iliopsoas which inserts into the lesser trochanter of the femur.

Along with the adductors, it slows extension at the hip at the end of support phase, and it initiates flexion of the hip for swing phase.
It may also laterally flex the lumbar vertebral column.

It is innervated by direct branches of L2-L4 ventral rami."""
psoas_major=fc.Muscle("Psoas Major", "Lateral Surface of Lumbar Vertebral Column", "Lesser Trochanter of Femur", "Laterally Flexes Lumbar Vert Column; with Iliacus and Hip Adductors, Slows Hip Extension at End of Support Phase, Initiates Hip Flexion at Beginning of Swing Phase", "Direct Branches of L2-L4 Ventral Rami", psoas_major_notes)
iliacus_notes="""Iliacus originates from the iliac fossa and, along with Psoas Major, inserts into the lesser trochanter of the femur.

Along with the adductors, it slows extension at the hip at the end of support phase, and it initiates flexion of the hip for swing phase.

It is innervated by the femoral nerve."""
iliacus=fc.Muscle("Iliacus", "Iliac Fossa", "Lesser Trochanter of Femur", "with Psoas Major and Hip Adductors, Slows Hip Extension at End of Support Phase, Initiates Hip Flexion at Beginning of Swing Phase", "Femoral Nerve", iliacus_notes)
quad_lumb_notes="""The Quadratus Lumborum originates from the lower edge of the 12th rib and the tips of the lumbar transverse processes.

It inserts into the iliac crest lateral to the sacral articulation.

It laterally flexes the lumbar vertebral column.

It is innervation by direct branches of L1-L4 ventral rami."""
quad_lumb=fc.Muscle("Quadratus Lumborum", "Lower Edge of 12th Rib and Tips of Lumbar Transverse Processes", "Iliac Crest Lateral to Sacral Articulation", "Laterally Flexes Lumbar Vertebral Column", "Direct Branches of L1-L4 Ventral Rami", quad_lumb_notes)
pubococcygeus_notes="""Pubococcygeus forms part of Levator Ani, along with Iliococcygeus. It originates from the inner surface of the pubic body
and it inserts along a midline raphe where it meets the contralateral Pubococcygeus.

The Levator Ani, along with Coccygeus, forms the Pelvic Diaphragm. It enables an increase in intra-abdominal pressure by resisting downward displacement.
The Pelvic Diaphragm has a long midline opening — the anourogential hiatus — for passage of the urethra, vagina (in females), and rectum into the perineum.
The fascial margin of this hiatus is attached to the walls of structures passing through it and to a wedge of connective tissue callen the perineal body.

It is innervated by branches of S3-S4 ventral rami superiorly, and possibly twigs from branches of the pudendal nerve inferiorly."""
pubococcygeus=fc.Muscle("Pubococcygeus", "Pubic Body", "Midline Raphe", "Enables Increase in Intra-Abdominal Pressure by Resisting Displacement", "S3-S4 Ventral Rami Superiorly, Possibly Pudendal Nerve Inferiorly", pubococcygeus_notes)
iliococcygeus_notes="""Iliococcygeus forms part of Levator Ani, along with Pubococcygeus. It originates from the Arcus Tendineus (a thickened band of
Obturator Internus fascia), and inserts along a midline raphe where it meets the contralateral Iliococcygeus.

The Levator Ani, along with Coccygeus, forms the Pelvic Diaphragm. It enables an increase in intra-abdominal pressure by resisting downward displacement.
The Pelvic Diaphragm has a long midline opening — the anourogential hiatus — for passage of the urethra, vagina (in females), and rectum into the perineum.
The fascial margin of this hiatus is attached to the walls of structures passing through it and to a wedge of connective tissue callen the perineal body.

It is innervated by branches of S3-S4 ventral rami superiorly, and possibly twigs from branches of the pudendal nerve inferiorly."""
iliococcygeus=fc.Muscle("Iliococcygeus", "Arcus Tendineus", "Midline Raphe", "Enables Increase in Intra-Abdominal Pressure by Resisting Displacement", "S3-S4 Ventral Rami Superiorly, Possibly Pudendal Nerve Inferiorly", iliococcygeus_notes)
coccygeus_notes="""The Coccygeus arises from the Ischial Spine and inserts onto the Coccyx and Sacrum. It is a vestige of a tail muscle.

Coccygeus, along with Levator Ani, forms the Pelvic Diaphragm. It enables an increase in intra-abdominal pressure by resisting downward displacement.
The Pelvic Diaphragm has a long midline opening — the anourogential hiatus — for passage of the urethra, vagina (in females), and rectum into the perineum.
The fascial margin of this hiatus is attached to the walls of structures passing through it and to a wedge of connective tissue callen the perineal body.

It is innervated by branches of S3-S4 ventral rami superiorly, and possibly twigs from branches of the pudendal nerve inferiorly."""
coccygeus=fc.Muscle("Coccygeus", "Ischial Spine", "Coccyx and Sacrum", "Enables Increase in Intra-Abdominal Pressure by Resisting Displacement", "S3-S4 Ventral Rami Superiorly, Possibly Pudendal Nerve Inferiorly", coccygeus_notes)
puborectalis_notes="""This muscle is applied to the inferior surface of the pubococcygeus. Each Puborectalis arises from the pubic body and sweeps
backward to meet its parter of the opposite side behind the rectum, forming a puborectal sling.

Pulls the posterior wall of the anal canal anteriorly against the anterior wall. It helps to maintain fecal continence; must be relaxed during defecation.

It is innervated by branches of S3-S4 ventral rami superiorly, and possibly twigs from branches of the pudendal nerve inferiorly."""
puborectalis=fc.Muscle("Puborectalis", "Pubic Body", "Left and Right Sides Continuous; N/A", "Enables Increase in Intra-Abdominal Pressure by Resisting Displacement", "S3-S4 Ventral Rami Superiorly, Possibly Pudendal Nerve Inferiorly", puborectalis_notes)
ischio_notes="""Ischiocavernosus covers the external surfaces of each crus. It is responsible for the rigid phase of erection by raising intraerectile
pressure to levels far greater than arterial pressure.

It is innervated by the perineal nerve."""
ischio=fc.Muscle("Ischiocavernosus", "Lies on Crus of Phallus", "Lies on Crus of Phallus", "Raises Intraerectile Pressure", "Perineal Nerve", ischio_notes)
bulbo_notes="""In males, the Bulbospongiosus covers the bulb of the penis and proximal part of the corpus spongiosum, meeting in a midline raphe on the
ventral surface of the bulb. In addition to a limited function in penile erection, the muscle assists in expusion of semen and urine. The right and left
Bulbospongiosus muscles of females are separate. Each covers the lateral surface of a bulb of the vestibule. Their function is unknown

It is innervated by the perineal nerve."""
bulbo=fc.Muscle("Bulbospongiosus", "Lies on Bulb of Phallus", "Lies on Bulb of Phallus", "Assists in Penile Erection and Explusion of Semen and Urine in Males; Unknown in Females", "Perineal Nerve", bulbo_notes)
sup_trans_per_notes="""On each side it arises from the anterior limit of the iscial tuberosity and passes medially to insert into the perineal body.
Its function is unknown.

It is innervated by the perineal nerve."""
sup_trans_per=fc.Muscle("Superficial Transvers Perineus", "Ischial Tuberosity", "Perineal Body", "Unknown", "Perineal Nerve", sup_trans_per_notes)
ext_anal_sphin_notes="""The External Anal Sphincter, innervated by the inferior rectal nerve, arises from the perineal body, sweeps around both sides
of the lower end of the anal canal, and inserts into the coccyx. Along with the puborectalis, it is responsible for voluntary control of fecal continence."""
ext_anal_sphin=fc.Muscle("External Anal Sphincter", "Perineal Body", "Coccyx", "Voluntary Fecal Continence", "Inferior Rectal Nerve", ext_anal_sphin_notes)
sphin_ureth_notes="""The Sphincter Urethrae (in both sexes) and the Sphincter Urethrovaginalis (in Females) surrounds the urethra above the perineal membrane.
It is thicker below the pelvic diaphragm, as it rests directly on the superior surface of the perineal membrane. In females, this lower part of the muscle
encircles both the urethra and the vagina. It is innervated by the Dorsal Nerve of the Phallus."""
sphin_ureth=fc.Muscle("Sphincter Urethrae (and Urethrovaginalis)", "Surrounds Urethra (and Vagina)", "Surrounds Urethra (and Vagina)", "Voluntary Continence", "Dorsal Nerve of the Phallus", sphin_ureth_notes)
deep_trans_per_notes="""In males, there is supposedly a Deep Transverse Perineus muscle, superior to the Perineal Membrane. It runs from the ischial tuberosity
to the perineal body and is innervated by the Dorsal Nerve of the Phallus."""
deep_trans_per=fc.Muscle("Deep Transverse Perineus", "Ischial Tuberosity", "Perineal Body", "Unknown", "Dorsal Nerve of the Phallus", deep_trans_per_notes)
comp_ureth_notes="""The Compressor Urethrae is a muscle in Females. It arises from the ischial tuberosity and meets its contralateral partner anterior to the
urethra, interdigitating with fibers of Sphincter Urethrovaginalis. It is innervated by the Dorsal Nerve of the Phallus."""
comp_ureth=fc.Muscle("Compressor Urethrae", "Ischial Tuberosity", "Interdigitates with Sphincter Urethrovaginalis", "Voluntary Continence", "Dorsal Nerve of the Phallus", comp_ureth_notes)
platysma_notes="""Platysma originates from the deep fascia over the upper Pectoralis Major and inserts into the lower border of the mandible and the skin of
the lower face and lower lip.

Platysma pulls the corner of the mouth down, as in a grimace.

It is innervated by the cervical branch of the facial nerve."""
platysma=fc.Muscle("Platysma", "Deep Fascia over Pectoralis Major", "Lower Border of Mandible and Skin of Lower Face and Lip", "Pulls Corners of the Mouth Down", "Cervical Branch of Facial Nerve", platysma_notes)
sternocleido_notes="""The sternal head of Sternocleidomastoid originates by a tendon from the manubrium, while the clavicular head arises from the medial
third of the clavicle. It inserts on the mastoid process and the lateral part of the superior nuchal line.

Acting unilaterally, Sternocleidomastoid rotates the head to face contralaterally and it laterally flexes the neck. Acting bilaterally, it flexes the neck
and it may weakly extend the atalnto-occipital joint.

It is innervated by the Accesory Nerve and direct branches from C2-C3 ventral rami."""
sternocleido=fc.Muscle("Sternocleidomastoid", "Sternal Head: By a Tendon From the Manubrium; Clavicular Head: Medial Third of Clavicle", "Mastoid Process and Lateral Part of Superior Nuchal Line", "Unilaterally: Rotates Head to Face Contralaterally and Laterally Flexes Neck; Bilaterally: Flexes Neck and May Weakly Extend Atlanto-Occipital Joint", "Accessory Nerve and Direct Branches from C2-C3 Ventral Rami", sternocleido_notes)
lev_scap_notes="""The Levator Scapulae originates from the C1-C4 vertebrae (posterior tubercles of transverse processes) and inserts into the vertebral border
of the scapula superior to the root of the scapular spine.

It pulls the superior angle of the scapula upward and anteriorly, as in extension of arm or reaching far forward.

It is innervated by C3-C4 ventral rami."""
lev_scap=fc.Muscle("Levator Scapulae", "C1-C4 Vertebrae (Posterior Tubercles of Transverse Processes)", "Vertebral Border of Scapula Superior to Root of Scapular Spine", "Pulls Superior Angle of Scapula Upward and Anteriorly, as in Extension of Arm or Reaching Far Forward", "C3-4 Ventral Rami", lev_scap_notes)
sternohyoid_notes="""Sternohyoid runs from the back of the manubrium and the medial end of the clavicle to the body of the hyoid.

It pulls the hyoid bone inferiorly; like the other strap muscles it is used to produce inferior displacements of the laryngeal apparatus that accompany vocalization and the last stage of swallowing."""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")
_notes=""""""
[muscle]=fc.Muscle("Name", "Origin", "Insertion", "Action", "Innervation", "Notes")