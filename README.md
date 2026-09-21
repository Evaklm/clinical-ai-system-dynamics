# Sustaining Clinical AI After Deployment

An exploratory system dynamics model of how technical performance, clinician trust and use, workflow conditions, and organizational response interact after clinical AI deployment.

> **Research in progress:** This repository is a protected public overview. The complete Model v2 implementation, parameter specification, experiments, and manuscript materials will be released after publication or preprint.

## Research question

How do changes in AI technical performance, clinician trust and use, and organizational monitoring and maintenance interact over time to determine whether a deployed clinical AI system remains sustainably used?

## Motivation

Strong pre-deployment validation does not guarantee that a clinical AI system will remain reliable or meaningfully used in practice. Performance can change after deployment, clinician trust and workflow fit evolve through experience, and organizational monitoring does not automatically translate into effective corrective action.

This project treats sustainability as a dynamic outcome produced by feedback among technical, human, and organizational mechanisms.

## Conceptual structure

```mermaid
flowchart TD
    P["AI performance"] --> T["Clinician trust"]
    T --> U["Actual AI use"]
    U --> B["Clinical and organizational benefit"]
    B --> O["Organizational support"]
    O --> M["Monitoring and maintenance"]
    M --> P
    U --> W["Workflow burden"]
    W --> T
```

The model represents six evolving states:

- AI performance
- clinician trust
- actual AI use
- organizational support
- maintenance capacity
- detected performance concern

## Analysis

The project uses:

- stock-and-flow modeling;
- numerical simulation of post-deployment feedback;
- isolated and combined intervention scenarios;
- verification and behavioral tests;
- sensitivity and uncertainty analysis;
- cautious, conditional interpretation rather than hospital-specific forecasting.

The intervention scenarios examine monitoring speed, corrective capacity, workflow support, clinician-facing support, organizational weakness, and coordinated policy packages.

## Research contribution

Existing work often examines technical drift, clinician acceptance, or organizational adoption separately. This project explores their interaction within one quantitative post-deployment lifecycle model.

The contribution is explanatory rather than predictive: it investigates the conditions under which feedback and delays can support recovery, persistent decline, or functional abandonment.

## Evidence and limitations

The causal structure and plausible parameter ranges are informed by published research. Where transferable empirical estimates are unavailable, values are treated explicitly as assumptions and tested across ranges.

The model:

- uses no patient-level data;
- is not calibrated to a specific hospital;
- does not predict the future performance of a particular clinical system;
- is intended for mechanism exploration and policy analysis.

## Tools

Python · NumPy · pandas · SciPy · Matplotlib · System dynamics · Monte Carlo analysis

## Release scope

The complete equations, final parameters, Model v2 notebook, detailed simulation results, and manuscript report remain private while the research is prepared for publication.

## Status

Model development and initial verification are complete. Literature validation and manuscript preparation are in progress.
