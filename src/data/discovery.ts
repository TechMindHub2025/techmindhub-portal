/** Reader-facing navigation. The ten canonical editorial domains remain unchanged. */
export const categories = [
  { id: "ai", label: "AI & Intelligent Systems", description: "Models, agents, evaluation and applied machine learning.", domains: ["ai"] },
  { id: "infrastructure", label: "Infrastructure & Cloud", description: "Compute, networks, data centres and operational systems.", domains: ["infrastructure"] },
  { id: "software", label: "Software & Developer Tools", description: "Engineering tools, platforms and open-source ecosystems.", domains: ["software"] },
  { id: "security", label: "Security & Digital Trust", description: "Cybersecurity, trust boundaries and technology governance.", domains: ["digital-trust"] },
  { id: "robotics", label: "Robotics & Automation", description: "Autonomous systems, control and industrial automation.", domains: ["robotics"] },
  { id: "physical-computing", label: "Quantum, Photonics & Space", description: "Optics, quantum devices, astronomy and space systems.", domains: ["photonics", "space"] },
  { id: "materials-energy", label: "Materials & Energy", description: "New materials, manufacturing, energy and the environment.", domains: ["materials", "energy-environment"] },
  { id: "life-sciences", label: "Life Sciences & Health", description: "Biotechnology, medical research and health technologies.", domains: ["life-sciences"] },
] as const;

/** Curated by exact technical tags; articles may appear in multiple collections. */
export const collections = [
  {
    id: "ai-infrastructure", label: "AI Infrastructure",
    description: "How power, compute, networking and data-centre design shape AI deployment.",
    tags: ["AIInfrastructure", "DataCenters", "CloudInfrastructure", "OpticalNetworking", "ComputeGovernance"],
  },
  {
    id: "engineering-reliability", label: "Engineering Reliability",
    description: "Failure domains, observability, reproducibility and the evidence behind dependable systems.",
    tags: ["CloudReliability", "DistributedSystems", "IncidentAnalysis", "Observability", "WorkflowReliability", "Reproducibility", "SystemsEngineering"],
  },
  {
    id: "ai-governance", label: "AI Governance",
    description: "Model oversight, safety evidence, access policy and the institutions shaping AI use.",
    tags: ["AIGovernance", "AISafety", "AgentGovernance", "AITraining", "AIRegulation", "TechnologyPolicy"],
  },
] as const;

export function categoryForDomain(domain?: string) {
  return categories.find(category => (category.domains as readonly string[]).includes(domain ?? ""));
}

export function articleInCollection(tags: readonly string[], collectionTags: readonly string[]) {
  return tags.some(tag => collectionTags.includes(tag));
}
