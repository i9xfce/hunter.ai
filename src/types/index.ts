export type Domain='Cloud Concepts'|'Security and Compliance'|'Cloud Technology and Services'|'Billing, Pricing and Support';
export type Question={id:number;domain:Domain;service:string;difficulty:'Easy'|'Medium'|'Hard';question:string;options:string[];answer:'A'|'B'|'C'|'D';explanation:string;keywords:string[]};
export type Violation={type:string;at:string}; export type Attempt={id:string;answers:Record<number,string>;marked:number[];violations:Violation[];startedAt:string;mode:'official'|'study'};
