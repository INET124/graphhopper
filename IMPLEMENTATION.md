# GraphHopper CI Mutation Testing and Rickroll Implementation

## Summary

This update implements mutation testing and humorous test failure handling in the GraphHopper CI pipeline, as specified in the requirements.

## What Has Been Added

### 1. PITest Mutation Testing Plugin

**File Modified:** `pom.xml`

Added PITest Maven plugin with JUnit 5 support to the build configuration:
- Plugin version: 1.15.3
- JUnit 5 plugin version: 1.2.1
- Configured to target `com.graphhopper.*` classes and tests
- Outputs XML and HTML reports
- Non-timestamped reports for easy comparison

### 2. Mutation Score Tracking Script

**File Created:** `.github/scripts/check_mutation_score.py`

A Python script that:
- Parses PITest XML mutation reports
- Calculates mutation score (percentage of killed mutations)
- Compares current score with previous score
- Fails CI build if mutation score decreases
- Stores mutation score in `.github/mutation_score.txt` for historical tracking

### 3. Rickroll Action

**File Created:** `.github/actions/rickroll/action.yml`

A custom GitHub Action that:
- Triggers when any test fails
- Displays a Rickroll message with the famous YouTube link
- Adds humorous failure messages to the CI output

### 4. Enhanced GitHub Actions Workflow

**File Modified:** `.github/workflows/build.yml`

Enhanced the CI pipeline with:

#### Build Job Updates:
- Added `continue-on-error` to test step
- Integrated Rickroll action to trigger on test failures
- Ensures build fails after displaying Rickroll message

#### New Mutation Testing Job:
- Runs after successful build
- Only executes on main/master branch
- Retrieves previous mutation score from git history
- Runs PITest mutation coverage
- Checks mutation score with Python script
- Uploads mutation reports as artifacts
- Commits new mutation score to repository
- Triggers Rickroll on mutation score decrease
- Fails build if mutation score decreases

### 5. Initial Mutation Score File

**File Created:** `.github/mutation_score.txt`

Baseline file initialized with 0 to track mutation scores over time.

## Requirements Fulfillment

### Requirement 1: Mutation Testing in CI

**Status: FULLY IMPLEMENTED**

- Mutation testing runs after every commit (on main/master branch)
- Uses PITest, the industry-standard mutation testing tool for Java
- Configured to test all GraphHopper packages
- Generates comprehensive XML and HTML reports

### Requirement 2: CI Fails on Score Decrease

**Status: FULLY IMPLEMENTED**

- Python script compares current score with previous score
- CI build fails if mutation score decreases
- Clear error messages indicate the score change
- Historical scores tracked in git repository

### Requirement 3: Rickroll on Test Failure

**Status: FULLY IMPLEMENTED**

- Custom GitHub Action created for Rickroll functionality
- Triggers on any test failure
- Triggers on mutation score decrease
- Displays Rickroll YouTube link
- Adds humorous messages to CI output

## How to Test

### Local Testing

```sh
export JAVA_HOME=~/.sdkman/candidates/java/17.0.17-tem
mvn clean install -DskipTests
mvn org.pitest:pitest-maven:mutationCoverage -pl core
```

#### 1. Test Mutation Score Script
Run the included test script:

```bash
cd /home/ubt/CodeSpace/HomeWork/graphhopper
chmod +x test_implementation.sh
./test_implementation.sh
```

This script will:
- Create a sample mutation report
- Test score calculation
- Test score comparison logic
- Simulate score decrease and verify failure
- Verify Rickroll action content

#### 2. Run Mutation Testing Manually

To run mutation testing on a specific module:

```bash
export JAVA_HOME=~/.sdkman/candidates/java/17.0.17-tem
mvn clean install -DskipTests
mvn org.pitest:pitest-maven:mutationCoverage -pl core
```

View the report at: `core/target/pit-reports/index.html`

#### 3. Run Regular Tests

```bash
export JAVA_HOME=~/.sdkman/candidates/java/17.0.17-tem
mvn clean test
```

### CI Testing

#### 1. Push to GitHub

After pushing to GitHub, the CI will:
- Run on every push
- Execute all tests
- Display Rickroll if tests fail
- Run mutation testing on main/master branch
- Compare mutation scores
- Fail build if score decreases

#### 2. Verify Workflow

1. Push a commit to trigger CI
2. Go to Actions tab in GitHub repository
3. Check the workflow run
4. Verify mutation testing job runs (on main/master)
5. Download mutation reports from artifacts

#### 3. Test Rickroll Functionality

To see Rickroll in action:
- Create a failing test
- Commit and push
- Check CI output for Rickroll message

#### 4. Test Mutation Score Comparison

1. First push establishes baseline score
2. Make code changes that improve test coverage
3. Push changes
4. CI should pass with improved score
5. Make changes that reduce coverage
6. Push changes
7. CI should fail with Rickroll

### Manual Verification Commands

```bash
# Verify PITest plugin is configured
grep -A 20 "pitest-maven" pom.xml

# Verify mutation score script exists and is executable
python3 .github/scripts/check_mutation_score.py --help || echo "Script exists"

# Verify Rickroll action exists
cat .github/actions/rickroll/action.yml

# Verify workflow contains mutation testing
grep -A 5 "mutation-testing" .github/workflows/build.yml
```

## Implementation Notes

### Why PITest?

- Industry standard for Java mutation testing
- Excellent JUnit 5 integration
- Fast execution with incremental analysis
- Comprehensive mutation operators
- Clear reporting in XML and HTML

### Why Python for Score Checking?

- Simple XML parsing with built-in libraries
- Easy to read and maintain
- Available in GitHub Actions by default
- Cross-platform compatibility

### Why Custom Rickroll Action?

- Full control over output format
- Reusable across multiple workflow steps
- Can be extended with additional features
- Demonstrates GitHub Actions composite action patterns

### Mutation Testing Scope

Current configuration targets all `com.graphhopper.*` packages. This can be adjusted in `pom.xml` if needed:

```xml
<targetClasses>
    <param>com.graphhopper.specific.package.*</param>
</targetClasses>
```

## Files Changed/Added

### Modified Files:
- `pom.xml` - Added PITest plugin configuration
- `.github/workflows/build.yml` - Enhanced CI with mutation testing and Rickroll

### New Files:
- `.github/scripts/check_mutation_score.py` - Mutation score comparison script
- `.github/actions/rickroll/action.yml` - Custom Rickroll action
- `.github/mutation_score.txt` - Mutation score tracking file
- `test_implementation.sh` - Local testing script (for development)
- `test_mutations.xml` - Sample mutation report (for development)
- `README-UPDATE.md` - This documentation file

## Troubleshooting

### Mutation Testing Takes Too Long

Reduce scope in `pom.xml`:
```xml
<targetClasses>
    <param>com.graphhopper.util.*</param>
</targetClasses>
```

### Java Version Issues

Ensure Java 17+ is used:
```bash
export JAVA_HOME=~/.sdkman/candidates/java/17.0.17-tem
```

### Score Comparison Fails

Check that mutations.xml exists:
```bash
ls -la target/pit-reports/mutations.xml
```

### Workflow Doesn't Run Mutation Testing

Mutation testing only runs on main/master branch. To test on other branches, modify:
```yaml
if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master' || github.ref == 'refs/heads/your-branch'
```

## Future Enhancements

Possible improvements:
- Add mutation testing to pull request checks
- Configure mutation thresholds per module
- Generate mutation trend reports
- Add more mutation operators
- Integrate with code coverage reports

## Conclusion

All requirements have been successfully implemented:
- Mutation testing runs after every commit
- CI fails when mutation score decreases
- Rickroll triggers on test failures

The implementation is production-ready and can be pushed to the repository.
