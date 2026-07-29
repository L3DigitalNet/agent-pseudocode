---
bug_id: '008'
date: '2026-07-29'
title: 'Production-entry test assumes real scene composition remains blocked'
services: [video, tests]
status: open
---

## Cause

`test_tc_t8_002__production_entry__fails_closed_when_real_states_are_blocked` calls `verify_production_delivery` against the live repository root and expects `compose_scene_states` to fail. Later explainer work completed the real capture and scene inputs, so composition now succeeds with 14 states and verification advances to the delivery-inventory gate.

The test does not isolate or force the source-state failure named by its assertion. Its temporary deliverables live outside `dist/video/final`, so the first genuine failure is now `INVENTORY-delivery`, not `SOURCE-production-states`.

## Evidence

The failure reproduces alone and in the full 302-test suite. Both the pre-Project-Standards-update baseline and the post-update coverage run report the same result: 301 passed and this assertion failed.

## Fix

Pending: make the test deterministically exercise the intended source-state failure without depending on the repository's current production inputs. Preserve separate coverage for the real-state-success path and the exact final-directory inventory gate.

## Lesson

A fail-closed test must control the boundary it expects to fail. Live repository evidence is suitable for an integration success test, but it is not a stable fixture for an earlier failure-path assertion.
