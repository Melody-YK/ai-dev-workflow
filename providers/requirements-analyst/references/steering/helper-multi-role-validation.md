---
inclusion: agent
---

# Multi-Role Validation Perspectives

In the **Validate** phase, requirements MUST be validated from multiple role perspectives to ensure completeness and feasibility. Each role brings unique concerns and validation criteria.

---

## Validation Dimensions by Role

### Product Manager (PM) Perspective

**Focus**: Business value and user alignment

| Dimension | Validation Questions |
|-----------|---------------------|
| **Business Value** | Does this requirement deliver clear business value? What's the ROI? |
| **User Need** | Does this solve a real user problem? Is the user pain point validated? |
| **Market Fit** | How does this compare to competitors? Is there market demand? |
| **Strategic Alignment** | Does this align with product vision and roadmap? |
| **Priority Justification** | Is the priority (MoSCoW/RICE) justified by business metrics? |
| **Success Metrics** | Are success metrics defined? How will we measure value delivered? |

**PM Validation Checklist**:
- [ ] Business case is clear and justified
- [ ] User personas and needs are validated
- [ ] Feature aligns with product strategy
- [ ] Success metrics are measurable
- [ ] Stakeholder buy-in is obtained

---

### Requirements Analyst (RA) Perspective

**Focus**: Completeness, clarity, and traceability

| Dimension | Validation Questions |
|-----------|---------------------|
| **Completeness** | Are all functional and non-functional requirements captured? |
| **Clarity** | Is each requirement unambiguous with only one interpretation? |
| **Consistency** | Are there conflicts between requirements? |
| **Traceability** | Can each requirement be traced to business goals? |
| **Boundary Conditions** | Are edge cases and error conditions defined? |
| **Dependencies** | Are all dependencies identified and documented? |

**RA Validation Checklist**:
- [ ] All requirements have unique IDs
- [ ] No ambiguous terms (e.g., "fast", "user-friendly")
- [ ] Main flow, alternate flows, and exception flows documented
- [ ] Boundary conditions explicitly stated
- [ ] Traceability matrix is complete
- [ ] No conflicting requirements

---

### Software Architect (SA) Perspective

**Focus**: Technical feasibility and system impact

| Dimension | Validation Questions |
|-----------|---------------------|
| **Technical Feasibility** | Can this be implemented with current technology stack? |
| **Architecture Impact** | How does this affect existing system architecture? |
| **Scalability** | Will this scale to expected load? What are the limits? |
| **Security** | What are the security implications? Authentication? Authorization? |
| **Performance** | Are performance requirements realistic and measurable? |
| **Integration** | What systems need to integrate? Are APIs defined? |
| **Technical Debt** | Does this introduce or reduce technical debt? |

**SA Validation Checklist**:
- [ ] NFRs (performance, security, scalability) are quantified
- [ ] Architecture constraints are identified
- [ ] Integration points are documented
- [ ] No impossible or impractical requirements
- [ ] Technology choices are justified
- [ ] Security requirements are OWASP-aligned

---

### Software Engineer (SE) Perspective

**Focus**: Implementation clarity and effort estimation

| Dimension | Validation Questions |
|-----------|---------------------|
| **Implementation Clarity** | Is it clear how to implement this? |
| **Effort Estimation** | Can development effort be estimated accurately? |
| **Technical Constraints** | Are technical constraints and limitations documented? |
| **Error Handling** | What happens when things go wrong? |
| **Data Validation** | What input validation rules apply? |
| **Logging & Monitoring** | What needs to be logged or monitored? |
| **Backward Compatibility** | Does this break existing functionality? |

**SE Validation Checklist**:
- [ ] Implementation approach is clear
- [ ] Data models and schemas are defined
- [ ] Error handling scenarios are specified
- [ ] Input validation rules are documented
- [ ] No hidden complexity or ambiguity
- [ ] Backward compatibility is addressed

---

### Test Engineer (TE) Perspective

**Focus**: Testability and quality assurance

| Dimension | Validation Questions |
|-----------|---------------------|
| **Testability** | Can this requirement be tested? How? |
| **Acceptance Criteria** | Are acceptance criteria in GWT format and verifiable? |
| **Test Coverage** | What test types are needed? (Unit, Integration, E2E, Performance) |
| **Test Data** | What test data is required? |
| **Edge Cases** | Are edge cases and boundary conditions testable? |
| **Regression Impact** | What existing tests might be affected? |
| **Automation Feasibility** | Can tests be automated? |

**TE Validation Checklist**:
- [ ] Every requirement has acceptance criteria (GWT)
- [ ] Happy path scenarios defined
- [ ] Error scenarios defined (at least 2-3 per requirement)
- [ ] Edge cases identified and testable
- [ ] Performance test criteria specified (if applicable)
- [ ] Test data requirements documented

---

## Multi-Role Validation Process

### Step 1: Individual Role Review
Review requirements from each role's perspective using the checklists above.

### Step 2: Cross-Role Conflict Detection
Identify conflicts between role perspectives:

| Conflict Type | Example | Resolution Approach |
|---------------|---------|---------------------|
| **PM vs SA** | PM wants feature, SA says infeasible | Negotiate scope or timeline |
| **RA vs SE** | RA defines requirement, SE says unclear | Clarify implementation details |
| **SA vs TE** | SA designs system, TE says untestable | Adjust design for testability |
| **PM vs TE** | PM prioritizes speed, TE needs quality | Balance scope, time, quality |

### Step 3: Consolidated Validation Report
Create a validation report summarizing findings from all perspectives:

```markdown
## Multi-Role Validation Report

### Requirement: [REQ-XXX]

| Role | Status | Issues | Recommendations |
|------|--------|--------|-----------------|
| PM   | ✅/⚠️/❌ | [Issues] | [Recommendations] |
| RA   | ✅/⚠️/❌ | [Issues] | [Recommendations] |
| SA   | ✅/⚠️/❌ | [Issues] | [Recommendations] |
| SE   | ✅/⚠️/❌ | [Issues] | [Recommendations] |
| TE   | ✅/⚠️/❌ | [Issues] | [Recommendations] |

### Overall Status: [APPROVED / NEEDS REVISION / REJECTED]

### Action Items:
1. [Action item from validation]
2. [Action item from validation]
```

---

## Validation Question Templates

Use these templates when validating requirements:

### From PM Perspective:
> "As a Product Manager, I need to understand: What user problem does [REQ-XXX] solve, and how will we measure its success?"

### From RA Perspective:
> "As a Requirements Analyst, I need to verify: Is [REQ-XXX] complete, unambiguous, and traceable to business goals?"

### From SA Perspective:
> "As a Software Architect, I need to assess: Is [REQ-XXX] technically feasible within our architecture, and what are the NFR implications?"

### From SE Perspective:
> "As a Software Engineer, I need to clarify: How will [REQ-XXX] be implemented, and what are the error handling requirements?"

### From TE Perspective:
> "As a Test Engineer, I need to confirm: How will [REQ-XXX] be tested, and are the acceptance criteria verifiable?"
