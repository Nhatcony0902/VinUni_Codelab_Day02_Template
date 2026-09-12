Tên nhóm: B2
Họ và tên: Trần Đình Hinh
Mã sv: 2A202602399
#Email: 26ai.hinhtd@vinui.edu.vn

# Lab 02 - Deep Dive Report

# Use Case

## Xanh SM - AI-Assisted EV Charging Incident Support

---

# Phase 3 - Deep Dive

## 3.1 Current-State Workflow

When a driver experiences a low-battery or charging incident,
the current workflow is:

1. Driver reports the incident.
2. Dispatcher receives the request.
3. Dispatcher checks the vehicle location.
4. Dispatcher searches for nearby charging stations.
5. Dispatcher checks whether the station is appropriate.
6. Dispatcher writes instructions to the driver.
7. If no suitable station is available, dispatcher contacts
   the rescue/mobile charging team.

Estimated total processing time: approximately 15 minutes per incident.

### Main Bottleneck

The main bottleneck is the manual search and synthesis of charging
options and the creation of instructions for the driver.

---

# 3.2 Problem Statement

## 1. Actor / Operator

The primary operator is the Xanh SM dispatcher.
The driver is the affected frontline stakeholder.

## 2. Current Workflow

The driver reports a charging or low-battery incident.
The dispatcher manually checks the vehicle location, searches for
available charging options, determines whether the option is
appropriate, and sends instructions or escalates to the rescue team.

## 3. Bottleneck

Manual information retrieval and instruction drafting take
approximately 12 minutes of the 15-minute workflow.

The dispatcher must combine multiple pieces of information before
making a recommendation.

## 4. Business Impact

The long response time can increase driver waiting time,
increase dispatcher workload during peak hours, and potentially
increase trip disruption and customer cancellation risk.

For the prototype, we use 15 minutes per incident as a working
baseline assumption. This number should be replaced by operational
data before production deployment.

## 5. Success Metric

Primary metric:

Reduce average incident handling time from approximately
15 minutes to less than 3 minutes.

Secondary metrics:

- At least 95% of generated drafts contain the correct vehicle
  status information.
- 100% of critical-battery cases trigger the defined safety rule.
- 100% of outgoing instructions receive dispatcher review.

## 6. Operational Boundary

The AI assistant is a dispatcher co-pilot.

The AI MAY:

- summarize the incident;
- identify the reported battery level;
- suggest an appropriate charging option;
- generate a draft instruction;
- recommend escalation to mobile charging/rescue.

The AI MUST NOT:

- directly send instructions to the driver;
- bypass dispatcher review;
- recommend a charging station farther than 5 km when battery
  is below 5%;
- fabricate station availability;
- override operational safety rules.

Every response must remain a draft for human review.

---

# 3.3 AI Fit

## Option 1 - Rule / State Machine

Rules are useful for deterministic safety constraints.

Example:

IF battery < 5%
THEN do not recommend a station > 5 km
AND recommend mobile charging / rescue.

Advantages:

- deterministic;
- auditable;
- predictable.

Limitations:

- difficult to handle natural-language incident descriptions;
- difficult to summarize information;
- difficult to generate natural instructions.

## Option 2 - LLM Feature

The LLM can:

- understand natural-language driver reports;
- summarize incident information;
- generate a draft instruction;
- explain why escalation may be required.

This is the most suitable architecture for the prototype.

## Option 3 - Agentic Loop

A full autonomous agent could observe vehicle status,
search charging tools, compare options, contact dispatch tools,
and repeat the process.

However, this is not necessary for the first prototype.

The workflow is mostly structured and the operational risk is high.

Therefore, the current recommendation is:

### GO with Rule + LLM Feature + Human-in-the-loop.

### NOT YET for a fully autonomous Agent.

---

# 3.4 Future-State Workflow

Driver reports incident
        ↓
System receives incident
        ↓
🔵 LLM extracts incident information
        ↓
🔵 Rule engine checks safety constraints
        ↓
Battery < 5%?
      /       \
    YES        NO
     ↓          ↓
Mobile      Candidate
charger     charging station
     ↓          ↓
     └────┬─────┘
          ↓
🔵 LLM creates draft instruction
          ↓
🟢 Dispatcher reviews
       /       \
   APPROVE     REJECT/EDIT
      ↓            ↓
 Driver receives   Manual handling
 instruction

