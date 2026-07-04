# TwinPA

### A Modular Digital Twin Framework for Photoacoustic Imaging, Forward Modeling, and Reconstruction

TwinPA is a physics-driven digital twin framework designed for simulation, acquisition modeling, and image reconstruction in photoacoustic (optoacoustic) imaging systems.

The framework provides an end-to-end computational pipeline that models the complete signal formation process—from tissue phantom generation and optical fluence estimation to acoustic propagation, detector response simulation, and image reconstruction.

TwinPA was built to support research and development in computational imaging, inverse problems, biomedical imaging, and AI-assisted reconstruction validation.

---

## Core Capabilities

### Phantom Generation

* Synthetic tissue geometry creation
* Multi-material tissue property assignment
* Spatial property map generation for heterogeneous media

### Optical Forward Model

* Light fluence estimation inside tissue
* Optical absorption modeling
* Energy deposition simulation

### Pressure Generation Model

* Initial pressure rise computation
* Photoacoustic source map generation

### Acoustic Forward Model

* Ultrasound propagation simulation
* Detector array modeling
* Time-domain signal acquisition
* Detector impulse response simulation

### Reconstruction Pipeline

* Delay-and-sum beamforming reconstruction
* Sinogram generation
* Image formation from measured acoustic traces

### Visualization

* Ground-truth visualization
* Pressure map plotting
* Sinogram rendering
* Reconstruction analysis

---

## Repository Architecture

```text
core/
digital_twin/
    phantom/
    optical_model/
    pressure_model/
    acoustic_model/
reconstruction/
visualization/
tests/
```

The architecture follows a modular scientific software design, enabling independent replacement or extension of:

* optical solvers
* acoustic propagators
* reconstruction algorithms
* detector models

This design allows future integration of:

* finite element solvers
* GPU acceleration
* differentiable simulators
* machine learning reconstruction pipelines
* uncertainty quantification modules

---

## Engineering Highlights

* Object-oriented modular architecture
* Test-driven development using unit tests
* Reproducible simulation pipeline
* Separation of physics modules for maintainability
* Extensible design suitable for digital twin development

---

## Applications

TwinPA can support:

* Biomedical imaging research
* Computational imaging algorithm benchmarking
* Synthetic dataset generation
* Detector design optimization
* Reconstruction validation
* Physics-informed AI development



TwinPA bridges physics-based simulation and computational reconstruction, enabling reproducible digital twin development for next-generation photoacoustic imaging systems.
