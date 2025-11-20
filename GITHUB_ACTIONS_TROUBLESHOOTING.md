# GitHub Actions Troubleshooting Guide

## Problem: Actions not running after push

### Step 1: Check if Actions are enabled

1. Go to https://github.com/INET124/graphhopper
2. Click on **Settings** tab
3. Click on **Actions** in left sidebar
4. Under **Actions permissions**, ensure **Allow all actions and reusable workflows** is selected
5. Click **Save** if you made changes

### Step 2: Verify workflow files

Check if workflow files exist:
- `.github/workflows/build.yml` - Main build and test workflow
- `.github/workflows/test-simple.yml` - Simple test workflow

### Step 3: Check Actions tab

1. Go to https://github.com/INET124/graphhopper/actions
2. You should see workflow runs listed
3. If empty, check:
   - Are you on the main or master branch?
   - Did you push the .github directory?

### Step 4: Verify the push

Check what was pushed:

```bash
cd /home/ubt/CodeSpace/HomeWork/graphhopper
git log --oneline -3
git ls-tree -r HEAD .github/workflows/
```

### Step 5: Manual trigger (if needed)

If workflows don't trigger automatically:

1. Go to https://github.com/INET124/graphhopper/actions
2. Select a workflow from the left sidebar
3. Click **Run workflow** button
4. Select branch and click **Run workflow**

### Step 6: Check for errors

If workflows appear but fail:

1. Click on the failed workflow run
2. Click on the failed job
3. Expand each step to see error messages
4. Common issues:
   - Java version not available (fixed: now using Java 17 and 21)
   - Permissions issues (fixed: added permissions to workflow)
   - Missing dependencies (should be cached)

## What I Fixed

1. **Java versions**: Changed from Java 24/25-ea to stable Java 17/21
2. **Permissions**: Added `permissions: contents: write` for mutation score commits
3. **Branch triggers**: Explicitly specified main/master branches
4. **Path fixes**: Fixed mutation report paths for multi-module project
5. **Simple test workflow**: Added test-simple.yml for basic verification

## Quick Test

After pushing these changes, try:

```bash
cd /home/ubt/CodeSpace/HomeWork/graphhopper
git add .
git commit -m "Fix GitHub Actions configuration"
git push
```

Then immediately check: https://github.com/INET124/graphhopper/actions

You should see a new workflow run appear within 5-10 seconds.

## Expected Behavior

### For every push to main/master:

1. **Build and Test** job runs:
   - Tests with Java 17
   - Tests with Java 21
   - If tests fail: Shows Rickroll message
   
2. **Mutation Testing** job runs (after build):
   - Runs PITest on core module
   - Compares mutation score with previous
   - If score decreases: Shows Rickroll and fails
   - If score improves/same: Commits new score

3. **Test Simple** job runs:
   - Quick verification that Actions work
   - Tests Rickroll action

## Verify on GitHub

1. Go to Actions tab: https://github.com/INET124/graphhopper/actions
2. You should see 3 workflows running
3. Click on each to see progress
4. Download artifacts (pit-reports) after completion

## If Still Not Working

Check repository settings:
- Ensure repository is not a fork (Actions may need approval on forks)
- Check if organization has Actions restrictions
- Verify you have write permissions to the repository

## Contact Support

If nothing works:
- Check GitHub Status: https://www.githubstatus.com/
- Review GitHub Actions documentation: https://docs.github.com/en/actions
