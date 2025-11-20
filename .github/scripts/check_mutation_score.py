#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys
import os

def parse_mutation_score(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    mutations = root.find('mutations')
    if mutations is None:
        if root.tag == 'mutations':
            mutations = root
        else:
            return None
    
    total = len(mutations.findall('mutation'))
    killed = len([m for m in mutations.findall('mutation') if m.get('status') == 'KILLED'])
    
    if total == 0:
        return 0.0
    
    return round((killed / total) * 100, 2)

def main():
    report_file = 'target/pit-reports/mutations.xml'
    score_file = '.github/mutation_score.txt'
    
    if not os.path.exists(report_file):
        print(f"Error: {report_file} not found")
        sys.exit(1)
    
    current_score = parse_mutation_score(report_file)
    if current_score is None:
        print("Error: Could not parse mutation score from report")
        sys.exit(1)
    
    print(f"Current mutation score: {current_score}%")
    
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            previous_score = float(f.read().strip())
        print(f"Previous mutation score: {previous_score}%")
        
        if current_score < previous_score:
            print(f"FAIL: Mutation score decreased from {previous_score}% to {current_score}%")
            sys.exit(1)
        elif current_score > previous_score:
            print(f"SUCCESS: Mutation score improved from {previous_score}% to {current_score}%")
        else:
            print(f"Mutation score unchanged at {current_score}%")
    else:
        print("No previous score found. This is the baseline.")
    
    with open(score_file, 'w') as f:
        f.write(str(current_score))
    
    print("Mutation score check passed!")

if __name__ == '__main__':
    main()
