import os

num = 0
for folder in os.listdir("clean_midi/"):
  for file in os.listdir("clean_midi/"+ folder):
      print("""%s/%s""" % (folder, file))
      # [os.replace(file, file.replace(" ", "_")) for file in files]
      orig = """clean_midi/%s/%s""" % (folder, file)
      orig_no_sp = orig.replace(" ", "\\ ")
      orig_no_sp = orig_no_sp.replace(")", "\)")
      orig_no_sp = orig_no_sp.replace("(", "\(")
      orig_no_sp = orig_no_sp.replace("\'", "\\'")
      os.system("cp %s data/%d.mid" % (orig_no_sp, num))
      num = num + 1
