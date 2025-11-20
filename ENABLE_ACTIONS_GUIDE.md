# How to Enable GitHub Actions

## You are seeing: "There are no workflow runs yet."

This means GitHub Actions is not enabled for your repository. Follow these steps:

## Step 1: Enable Actions in Repository Settings

1. Go to: **https://github.com/INET124/graphhopper/settings/actions**

2. Under **"Actions permissions"**, select one of these options:
   - ✅ **"Allow all actions and reusable workflows"** (RECOMMENDED)
   - OR **"Allow INET124 actions and reusable workflows"**

3. Click **Save** button

4. Scroll down to **"Workflow permissions"**, select:
   - ✅ **"Read and write permissions"**

5. Check the box:
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**

6. Click **Save** again

## Step 2: Enable Actions from Actions Tab

1. Go to: **https://github.com/INET124/graphhopper/actions**

2. If you see a message like "Workflows aren't being run on this forked repository":
   - Click the green **"I understand my workflows, go ahead and enable them"** button

## Step 3: Manually Trigger a Workflow

After enabling Actions, trigger a test workflow:

1. Go to: **https://github.com/INET124/graphhopper/actions**

2. Click on **"Test Simple"** in the left sidebar

3. Click the **"Run workflow"** dropdown button on the right

4. Select branch: **main**

5. Click the green **"Run workflow"** button

6. Wait 5-10 seconds, then refresh the page

7. You should see a yellow running icon or completed workflow

## Step 4: Verify Automatic Triggers Work

Make a small change and push to test automatic triggers:

```bash
cd /home/ubt/CodeSpace/HomeWork/graphhopper
echo "# Testing Actions" >> test_actions.txt
git add test_actions.txt
git commit -m "Test: trigger GitHub Actions"
git push
```

Then immediately check: https://github.com/INET124/graphhopper/actions

You should see new workflow runs appear!

## Common Issues and Solutions

### Issue 1: "Workflows aren't being run on this forked repository"

**Solution**: Click the green button to enable workflows on this fork.

### Issue 2: "Actions are disabled for this repository"

**Solution**: Go to Settings → Actions and enable them as described in Step 1.

### Issue 3: Workflows show but don't run

**Solution**: 
- Check if you're pushing to the correct branch (main or master)
- Verify workflow files are in `.github/workflows/` directory
- Check for YAML syntax errors

### Issue 4: Permission errors

**Solution**: 
- Go to Settings → Actions → General → Workflow permissions
- Select "Read and write permissions"
- Save changes

## Expected Workflows

After enabling, you should see these workflows:

1. **Build and Test** - Runs on every push to main/master
2. **Mutation Testing** - Runs after build on main/master  
3. **Test Simple** - Quick test to verify Actions work

## Need More Help?

If Actions still don't work after following all steps:

1. Check GitHub Status: https://www.githubstatus.com/
2. Review GitHub Docs: https://docs.github.com/en/actions/quickstart
3. Check repository visibility (Actions work on both public and private repos)

## Quick Checklist

- [ ] Actions enabled in repository settings
- [ ] Workflow permissions set to "Read and write"
- [ ] Clicked "Enable workflows" button (if shown)
- [ ] Manually triggered "Test Simple" workflow
- [ ] Pushed a test commit to verify automatic triggers
- [ ] Verified workflow files exist in `.github/workflows/`

Once Actions are enabled, all future pushes will automatically trigger the workflows!
